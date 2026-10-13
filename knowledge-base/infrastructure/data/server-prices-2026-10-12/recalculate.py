"""Recompute explicitly labelled server budget scenarios; no supplier quotes sent."""
from pathlib import Path
import json, math
ROOT=Path(__file__).resolve().parent
FX=7.00
VAT=.13
CONTINGENCY=.10
observations=[
 dict(id='P-A100',vendor='The Server Store',url='https://www.theserverstore.com/nvidia-hgx-8x-a100-80gb-sxm4-nvlink-gpu-server-zt-systems',observed='2026-10-12',currency='USD',price=94999,
      product='ZT Systems 4U HGX 8x A100 80GB SXM4',condition='Refurbished',cpu='2x AMD EPYC 7V12 64-core',ram_gb=1024,ram='16x64GB DDR4-2933',storage='No M.2 by default; 4x1TB NVMe option adds USD1116',network='ConnectX-6 200G included',power='6x3000W Titanium, rails included',warranty='90 days seller warranty',china_delivery_verified=False,
      caveats=['Default option values parsed from archived HTML. Listed stock not a shipping commitment.','NVLink HGX label is present; supplier topology/configuration to be confirmed.','Public listing and compliance form notice do not establish export permission.']),
 dict(id='P-H100',vendor='Exxact',url='https://configurator.exxactcorp.com/configure/TS4-193475697',observed='2026-10-12',currency='USD',price=319924,
      product='TensorEX TS4-193475697, 8x H100 80GB SXM5/NVSwitch',condition='Configured vendor system',cpu='2x EPYC9454 48-core',ram_gb=1536,ram='24x64GB DDR5-4800',storage='960GB U.2 option selected; drive quantity not exposed in extracted page',network='Intel X550 dual10GbE selected',power='6x3000W 3+3, six C19-C20 cables and rails selected',warranty='3yr parts/labor plus email/phone support',china_delivery_verified=False),
 dict(id='P-H200',vendor='Exxact',url='https://configurator.exxactcorp.com/configure/TS4-118380266',observed='2026-10-12',currency='USD',price=326524,
      product='TensorEX TS4-118380266, 8x H200 141GB SXM/NVSwitch',condition='Configured vendor system',cpu='2x EPYC9454 48-core',ram_gb=1536,ram='24x64GB DDR5-4800',storage='960GB U.2 option selected; drive quantity not exposed in extracted page',network='Intel X550 dual10GbE selected',power='6x3000W 3+3; configured estimate6845W, not measured draw',warranty='3yr parts/labor plus email/phone support',china_delivery_verified=False),
 dict(id='P-H200NVL',vendor='ViperaTech',url='https://viperatech.com/product/nvidia-h200-nvl-graphic-card-141-gb-passive-pcie-900-21010-0040-000',observed='2026-10-12',currency='USD',price=33500,
      product='900-21010-0040-000 H200 NVL 141GB passive PCIe, per card',condition='Out of stock; page also claims two-week shipping',warranty='Seller states3yr manufacturer warranty',china_delivery_verified=False),
]
for x in observations:x['cny_at_scenario_fx']=x['price']*FX;x['price_class']='C_foreign_posted_price_not_China_delivered_quote'
cases=[]
def add(id,gpu,components,service,ram,cpu,notes,source_ids,condition):
 lo,hi=[sum(v[i] for v in components.values()) for i in range(2)]
 total=[lo*(1+VAT+CONTINGENCY)+service[0],hi*(1+VAT+CONTINGENCY)+service[1]]
 cases.append(dict(id=id,gpu=gpu,condition=condition,cpu=cpu,host_ram_gb=ram,price_class='D_analytical_cash_budget',components_exvat_cny=components,delivery_and_incremental_local_support_tax_included_cny=service,
  hardware_exvat_cny=[lo,hi],hardware_vat_preparation=VAT,hardware_price_contingency=CONTINGENCY,total_cny=total,
  rounded_outward_wan_cny=[math.floor(total[0]/10000),math.ceil(total[1]/10000)],source_ids=source_ids,notes=notes,
  formula='hardware * (1 + 0.13 + 0.10) + tax-included incremental delivery/local-support preparation',
  china_delivery_verified=False,performance_validation='Separate deployment study; price alone does not establish a working runtime or service target'))
a100=(94999+1116)*FX
add('A1008-SXM-refurb','8x A10080 SXM4 / HGX-NVLink',{'seller_system_plus_4x1tb_nvme_option':[a100,a100],'storage_and_site_compatibility_allowance':[10000,30000]},[80000,150000],1024,'2x EPYC7V12',
 ['Refurbished,90-day base warranty. Increment includes three-year local support/repair provision and delivery as a D allowance, not a contract.','Existing authorized in-country equipment can use incremental reuse accounting; acquisition/replacement value is separately retained.','No cold GPU benchmark or transaction license assumed.'],['P-A100'],'Refurbished / existing-stock comparison')
for id,price,src,gpu in [('H1008-SXM',319924,'P-H100','8x H10080 SXM5 / NVSwitch'),('H2008-SXM',326524,'P-H200','8x H200141 SXM / NVSwitch')]:
 base=price*FX
 add(id,gpu,{'public_configured_system':[base,base],'additional_storage_and_site_network':[25000,60000]},[70000,150000],1536,'2x EPYC9454',
 ['Vendor base already contains CPU,RAM,GPU,fans/power,rails and stated3yr parts/labor; these are not charged again.','Additional storage/network is an independent25k–60k CNY scenario, not a claimed vendor option price.','Delivery/local on-site support preparation supplements the listed remote support; tariff pass-through is not presumed.','TwoTP4 instances and oneTP8 instance use the same8-GPU acquisition budget; host Engram replication and runtime capacity differ.'],[src],'Vendor-configured new-system comparison')
add('H2004-NVL','4x H200141 NVL / four-way bridge group',{'gpu_cards':[4*33500*FX,1600000],'pcie_server_platform':[100000,160000],'cpu_pair':[35000,55000],'ram_1tb':[128000,272000],'nvme_system_and_model_storage':[25000,45000],'network':[15000,30000],'power_cooling_cabling':[30000,50000],'nvlink_bridge_set':[10000,30000]},[40000,70000],1024,'2x Xeon6710E-class',
 ['D integrated4-card server, not an HPE OEM quotation. GPU lower bound uses current foreign listing;400k/card upper and host components retain explicitly labelled9/21 analytical allowances.','GPU vendor page is out of stock; two-week prose is not adopted as delivery evidence.','Four-way bridge topology and600W GPU cooling require supplier-certified BOM.','Do not substitute HGX/SXM performance data for NVL without checking clocks/interconnect/profile.'],['P-H200NVL','hardware-prices-2026-09-21.json/G5'],'Four-card integrated-server scenario')
r={'as_of':'2026-10-12','currency':'CNY','fx':{'USD_CNY':FX,'kind':'scenario_not_spot'},'source_packet':'TECH-087','observations':observations,'server_cases':cases,
 'scope_exclusions':['new rack/UPS/facility renovation','cross-node400G/InfiniBand switching','recurring power and operations staff','application/harness/model integration','commercial software/model licenses'],
 'shared_services':{'two_cpu_tool_workers_wan_cny':[12,26],'one_gateway_wan_cny':[6,13],'classification':'HistoricalD assumptions from9/23Agent plan; not refreshed supplier quotes','counting_rule':'Add only incremental tool/application nodes; do not count GPU-server host CPU/RAM again.'},
 'procurement':{'facts_as_of':'2026-10-12','rule':'2026-00789 effective2026-01-15 provides conditional case-by-case review for eligible exports from theUS; route/end-user/technical conditions apply.',
 'nvidia_disclosure':'FY2027Q2 Form10-Q reports limited permittedH200 shipments and continuingPRC restrictions;25%US inspection-import tariff not passed to customers in that disclosure.',
 'cost_treatment':'No automatic additional25%H200tariff line. Add transaction-specific supplier charges only if actually quoted and not already embedded.'},
 'comparison_notes':['Source prices are not China quotations or procurement authorization.','A100refurbished vs Hopperconfigured new has a support/age difference; show both price and condition.','No point estimate labelled best value before runtime/context/service constraints are applied.']}
for c in cases:
 for i in [0,1]:assert abs(c['total_cny'][i]-(sum(v[i] for v in c['components_exvat_cny'].values())*1.23+c['delivery_and_incremental_local_support_tax_included_cny'][i]))<1e-6
(ROOT.parent/'hardware-prices-2026-10-12.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
for c in cases:print(c['id'],c['rounded_outward_wan_cny'],c['total_cny'])
