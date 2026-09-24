Onyx’s Connectors create a bridge between your organization’s data sources and generative AI features in Onyx. Nearly all connectors are persistent and regularly sync changes from your source.

Both the data that is retrieved from the source and the data that your users can access through Onyx can be customized to your needs!

To find specific instructions for each Connector, see the [Supported Connectors](#supported-connectors) section.

![Onyx Add Connector page](https://mintcdn.com/danswer/sZSCgOqeRdUK59k_/assets/admins/connectors/add_connector.png?w=2500&fit=max&auto=format&n=sZSCgOqeRdUK59k_&q=85&s=61d7613855ae45002b5b4373b8fb73a7)

Onyx Add Connector page

## Adding a Connector

To add a new connector, navigate to the **Admin Panel** and click **Add Connector** in the sidebar. This page shows all officially supported connectors.

You can see unofficial, community-supported connectors by setting `SHOW_EXTRA_CONNECTORS=true` in your environment.

Click on any of the tiles to begin creating a new Connector.

### Credentials

Most Connectors require some form of authentication for Onyx to access your source. This authentication is called a Credential and differs by Connector.

![Onyx Connector Credentials page](https://mintcdn.com/danswer/aj13v1mzLf028SWE/assets/admins/connectors/generic_credentials.png?w=2500&fit=max&auto=format&n=aj13v1mzLf028SWE&q=85&s=71c63223ad1744a3e9ed9f7d093700cb)

Onyx Connector Credentials page

### Configuration

Each connector must be given a Name. Additionally, each Connector has its own configuration options to specify the data that should be indexed.

![Onyx Connector Configuration page](https://mintcdn.com/danswer/aj13v1mzLf028SWE/assets/admins/connectors/generic_config.png?w=2500&fit=max&auto=format&n=aj13v1mzLf028SWE&q=85&s=d685a454c18c3d9f4dd7e719496562fc)

Onyx Connector Configuration page

### Document Access Controls

Connectors can be configured to be **Private**, **Public**, or **Auto Sync Permissions**.

**Private**: Only the user who created the Connector may see data from this Connector in Onyx. You may also assign specific Users and User Groups access to this Connector’s data.

**Public**: All Onyx users may see data from this Connector.

If you configure the Connector to access private data in the source, all Onyx users will be able to see this data.

#### Permission-Syncing Connectors

If you set your Connector’s access type to **Auto Sync Permissions**, Onyx will maintain an access control list from the source and restrict users to only see data they have access to.

Permission-syncing is only available for the following Connectors:

- Confluence
- Jira
- Google Drive (must use service account or Google Workspace Admin OAuth credentials)
- Gmail (must use service account or Google Workspace Admin OAuth credentials)
- Slack (see Federated Slack documentation)
- Salesforce
- GitHub
- Box
- Canvas
- SharePoint (must use certificate-based authentication)
- Microsoft Teams
- Outlook

Permission-syncing connectors are an Enterprise Edition feature.

### Advanced Configuration

Clicking **Advanced Configuration** on the bottom left of the Connector configuration page will reveal additional, optional settings for indexing.

**Prune Frequency**: The frequency at which old data (that no longer exists in the source) should be removed from Onyx. This is set to 30 days by default.

**Refresh Frequency**: The frequency at which new data should be retrieved from the source. This is set to 30 minutes by default.

**Indexing Start Date**: The date and time from which data should be indexed (data created or updated before this date will not be indexed). This is set to the earliest possible date in the source by default.

![Onyx Connector Advanced Configuration page](https://mintcdn.com/danswer/aj13v1mzLf028SWE/assets/admins/connectors/generic_advanced_config.png?w=2500&fit=max&auto=format&n=aj13v1mzLf028SWE&q=85&s=6006b88ca2b2b561d0254875ebcb8337)

Onyx Connector Advanced Configuration page

## Managing Existing Connectors

To see your existing Connectors, navigate to the **Admin Panel** and click **Existing Connectors** in the sidebar. This page will show an overview of your Connectors, their status, and the amount of data they have indexed.

![Onyx Existing Connectors page showing connector statuses](https://mintcdn.com/danswer/24Ocig51qMqahMaT/assets/admins/connectors/indexing_status.png?w=2500&fit=max&auto=format&n=24Ocig51qMqahMaT&q=85&s=64af17a9f1ea1b36cd8092013da2fcc7)

Onyx Existing Connectors page showing connector statuses

### Connector Status

The status of a Connector can be:

#### Active

| Status | Description |
| --- | --- |
| **Indexed** | The Connector is fully functional and all data is synced as of the last indexing attempt. |
| **Scheduled** | Newly created Connectors or Connectors that have reached their refresh frequency but have not begun a new indexing attempt. |
| **Indexing / Initial Indexing** | The Connector is currently retrieving data from the source. |

#### Inactive or Semi-Active

| Status | Description |
| --- | --- |
| **Paused** | The Connector has been paused and will not retrieve new data until un-paused. Users can still access the indexed data. |
| **Error** | The Connector has encountered an error during indexing. Any data indexed prior to the error will remain available. Onyx will attempt to index again. If too many errors occur, the Connector will be paused. |

Most Error statuses are temporary and will resolve themselves naturally within a few hours. If you see an Error status that persists, please reach out.

### Connector Details

Clicking on an existing Connector will show you details about its configuration, status, and indexing attempts.

In the **Manage** menu, you can pause, resume, delete, or initiate a complete re-indexing of the Connector.

Under the **Advanced** section, you can see the prune and refresh settings, as well as the history of indexing attempts.

![Onyx Connector details page showing connector details](https://mintcdn.com/danswer/aj13v1mzLf028SWE/assets/admins/connectors/connector_details.png?w=2500&fit=max&auto=format&n=aj13v1mzLf028SWE&q=85&s=3a40a50a1e70de38520c08727e9fe974)

Onyx Connector details page showing connector details

![Onyx Connector details page showing indexing attempts and failures](https://mintcdn.com/danswer/24Ocig51qMqahMaT/assets/admins/connectors/indexing_attempts.png?w=2500&fit=max&auto=format&n=24Ocig51qMqahMaT&q=85&s=7bbddb8f70a68309b9c47348d0642e43)

Onyx Connector details page showing indexing attempts and failures

### Indexing Failures

Rarely, you will see a **Completed with errors** indexing attempt. If this happens, you can click the **Resolve all errors** button to kickoff a complete re-indexing of the Connector.

## Supported Connectors

Can’t find the connector you’re looking for? Let us know via [GitHub Discussions](https://github.com/onyx-dot-app/onyx/discussions)!