# writing a powershell module:
# http://msdn.microsoft.com/en-us/library/dd878310%28v=vs.85%29.aspx

# 31 days of azure:
# http://www.virtuallycloud9.com/index.php/31-days-of-servers-in-the-cloud-series/

if (Get-Module AzurePS) { return }

## Construct module
try
{
	Push-Location $PSScriptRoot
	. ./Provision.ps1
}
finally
{
	Pop-Location
}

## Export functions
Export-ModuleMember -function @(
	## Provisioning VMs
	'Deploy-VM'
	, 'Deprovision-VM'
)

#Set-Alias v3sGetSettings v3s-Get-Settings
#Export-ModuleMember -alias @(
#	'v3sGetSettings'
#)
