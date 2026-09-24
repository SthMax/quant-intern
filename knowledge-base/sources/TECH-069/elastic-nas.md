The *Elastic network drive connector* is a [connector](/docs/reference/search-connectors) for network drive data sources. This connector is written in Python using the [Elastic connector framework](https://github.com/elastic/connectors/tree/main).

View the [**source code** for this connector](https://github.com/elastic/connectors/tree/main/app/connectors_service/connectors/sources/network_drive) (branch *main*, compatible with Elastic *9.0*).

## Self-managed connector

### Availability and prerequisites

This connector is available as a self-managed connector. This self-managed connector is compatible with Elastic versions **8.6.0+**.

To use this connector, satisfy all [self-managed connector requirements](/docs/reference/search-connectors/self-managed-connectors).

### Usage

To use this connector as a **self-managed connector**, see [*Self-managed connectors*](/docs/reference/search-connectors/self-managed-connectors) For additional usage operations, see [*Connectors UI in Kibana*](/docs/reference/search-connectors/connectors-ui-in-kibana).

### Configuration

The following configuration fields are required to set up the connector:

`username`

The username of the account for the network drive. The user must have at least **read** permissions for the folder path provided.

`password`

The password of the account to be used for crawling the network drive.

`server_ip`

The server IP address where the network drive is hosted. Default value is `127.0.0.1`.

`server_port`

The server port where the network drive service is available. Default value is `445`.

`drive_path`

- The network drive path the connector will crawl to fetch files. This is the name of the folder shared via SMB. The connector uses the Python [`smbprotocol`](https://github.com/jborean93/smbprotocol) library which supports both **SMB v2** and **v3**.
- Accepts only one path— parent folders can be specified to widen the scope.
- The drive path should use **forward slashes** as path separators. Example:
- `admin/bin`

`use_document_level_security`

Toggle to enable document level security (DLS). When enabled:

- Full syncs will fetch access control lists for each document and store them in the `_allow_access_control` field.
- Access control syncs will fetch users' access control lists and store them in a separate index.

Refer to [Document level security](#es-connectors-network-drive-client-dls) for more information, including prerequisites and limitations.

`drive_type`

The type of network drive to be crawled. The following options are available:

- `Windows`
- `Linux`

`identity_mappings`

Path to a CSV file containing user and group SIDs (For Linux Network Drive).

File should be formatted as follows:

- Fields separated by semicolons (`;`)
- Three fields per line: `Username;User-SID;Group-SIDs`
- Group-SIDs are comma-separated and optional.

**Example** with one username, user-sid and no group:

`text user1;S-1; `

**Example** with one username, user-sid and two groups:

`text user1;S-1;S-11,S-22 `

### Deployment using Docker

You can deploy the Network drive connector as a self-managed connector using Docker. Follow these instructions.

Download the sample configuration file. You can either download it manually or run the following command:

```sh
curl https://raw.githubusercontent.com/elastic/connectors/main/app/connectors_service/config.yml.example --output ~/connectors-config/config.yml
```

Remember to update the `--output` argument value if your directory name is different, or you want to use a different config file name.

Update the configuration file with the following settings to match your environment:

- `elasticsearch.host`
- `elasticsearch.api_key`
- `connectors`

If you’re running the connector service against a Dockerized version of Elasticsearch and Kibana, your config file will look like this:

```yaml
# When connecting to your cloud deployment you should edit the host value
elasticsearch.host: http://host.docker.internal:9200
elasticsearch.api_key: <ELASTICSEARCH_API_KEY>

connectors:
  -
    connector_id: <CONNECTOR_ID_FROM_KIBANA>
    service_type: network_drive
    api_key: <CONNECTOR_API_KEY_FROM_KIBANA>
```

1. Optional. If not provided, the connector will use the elasticsearch.api\_key instead

Using the `elasticsearch.api_key` is the recommended authentication method. However, you can also use `elasticsearch.username` and `elasticsearch.password` to authenticate with your Elasticsearch instance.

Note: You can change other default configurations by simply uncommenting specific settings in the configuration file and modifying their values.

Run the Docker image with the Connector Service using the following command:

```sh
docker run \
-v ~/connectors-config:/config \
--network "elastic" \
--tty \
--rm \
docker.elastic.co/integrations/elastic-connectors:9.5.4 \
/app/bin/elastic-ingest \
-c /config/config.yml
```

Refer to [`DOCKER.md`](https://github.com/elastic/connectors/tree/main/docs/DOCKER.md) in the `elastic/connectors` repo for more details.

Find all available Docker images in the [official registry](https://www.docker.elastic.co/r/integrations/elastic-connectors).

> [!tip] Tip
> We also have a quickstart self-managed option using Docker Compose, so you can spin up all required services at once: Elasticsearch, Kibana, and the connectors service. Refer to this [README](https://github.com/elastic/connectors/tree/main/scripts/stack#readme) in the `elastic/connectors` repo for more information.

### Documents and syncs

The connector syncs folders as separate documents in Elasticsearch. The following fields will be added for the document type `folder`:

- `create_time`
- `title`
- `path`
- `modified`
- `time`
- `id`

> [!note] Note
> - Content from files bigger than 10 MB won’t be extracted
> - Permissions are not synced by default. You must first enable [DLS](#es-connectors-network-drive-client-dls). Otherwise, **all documents** indexed to an Elastic deployment will be visible to **all users with access** to that Elastic Deployment.

#### Sync types

[Full syncs](about:/docs/reference/search-connectors/content-syncs#es-connectors-sync-types-full) are supported by default for all connectors.

This connector also supports [incremental syncs](about:/docs/reference/search-connectors/content-syncs#es-connectors-sync-types-incremental).

### Document level security

Document Level Security (DLS) enables you to restrict access to documents based on a user’s permissions. DLS facilitates the syncing of folder and file permissions, including both user and group level permissions.

> [!note] Note
> **Note:** Refer to [DLS in Search Applications](/docs/reference/search-connectors/es-dls-e2e-guide) to learn how to search data with DLS enabled, when building a search application.

#### Availability

- The Network Drive self-managed connector offers DLS support for both Windows and Linux network drives.
- To fetch users and groups in a Windows network drive, account credentials added in the connector configuration should have access to the Powershell of the Windows Server where the network drive is hosted.

### Sync rules

[Basic sync rules](about:/docs/reference/search-connectors/es-sync-rules#es-sync-rules-basic) are identical for all connectors and are available by default.

#### Advanced sync rules

> [!note] Note
> A [full sync](about:/docs/reference/search-connectors/content-syncs#es-connectors-sync-types-full) is required for advanced sync rules to take effect.

Advanced sync rules are defined through a source-specific DSL JSON snippet. Advanced sync rules for this connector use **glob patterns**.

1. Each rule must contains a glob pattern. This pattern is then matched against all the available folder paths inside the configured drive path.
2. The pattern must begin with the `drive_path` field configured in the connector.
3. If the pattern matches any available folder paths, the contents directly within those folders will be fetched.

The following sections provide examples of advanced sync rules for this connector.

**Indexing files and folders recursively within folders**

```js
[
  {
    "pattern": "Folder-shared/a/mock/**"
  },
  {
    "pattern": "Folder-shared/b/alpha/**"
  }
]
```

**Indexing files and folders directly inside folder**

```js
[
  {
    "pattern": "Folder-shared/a/b/test"
  }
]
```

**Indexing files and folders directly inside a set of folders**

```js
[
  {
    "pattern": "Folder-shared/org/*/all-tests/test[135]"
  }
]
```

**Excluding files and folders that match a pattern**

```js
[
  {
    "pattern": "Folder-shared/**/all-tests/test[!7]"
  }
]
```

### Content extraction

See [Content extraction](/docs/reference/search-connectors/es-connectors-content-extraction).

### End-to-end tests

The connector framework enables operators to run functional tests against a real data source. Refer to [Connector testing](about:/docs/reference/search-connectors/self-managed-connectors#es-build-connector-testing) for more details.

To execute a functional test for the Network Drive self-managed connector, run the following command:

```shell
$ make ftest NAME=network_drive
```

By default, this will use a medium-sized dataset. For faster tests add the `DATA_SIZE=small` flag:

```shell
make ftest NAME=network_drive DATA_SIZE=small
```

There are no known issues for this connector.

See [Known issues](/docs/release-notes/elasticsearch/known-issues) for any issues affecting all connectors.

See [Troubleshooting](/docs/reference/search-connectors/es-connectors-troubleshooting).

### Security

See [Security](/docs/reference/search-connectors/es-connectors-security).