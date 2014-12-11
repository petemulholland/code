# Templating Azure VMs with Powershell:
# http://blogs.technet.com/b/keithmayer/archive/2013/01/17/step-by-step-templating-vms-in-the-cloud-with-windows-azure-and-powershell-31-days-of-servers-in-the-cloud-part-17-of-31.aspx

# $VMName = "PPMBaseVM01"
# $AffinityGroup = "PPMLab01"
# $ImageName = "PPMBaseVM01-PS-IIS"
# $ServiceName = "PPMBaseVM01" # same as first VM setup, but not required to be same as VM Name (If i change the VM name i'll still have to use existing cloud service)
# NOTE: if service already exists, can't specify affinityGroup, so could create new service in affinity group using the vm name.


# Get-Help New-AzureQuickVM
# New-AzureQuickVM -Windows -ServiceName <string> 
#							-ImageName <string> 
#							[-Name <string>] 
#							[-AffinityGroup <string>] 
#							[-InstanceSize <string>] 
#							[-AdminUsername <string>] 
#							[-Password <string>]
#
#						??	[-MediaLocation <string>] 
#						??	[-Location <string>] 
#
#							[-Certificates <CertificateSettingList>] 
#							[-WaitForBoot] 
#							[-ReverseDnsFqdn <string>] 
#							[-DisableWinRMHttps] 
#							[-EnableWinRMHttp] 
#							[-WinRMCertificate <X509Certificate2>] 
#							[-X509Certificates <X509Certificate2[]>] 
#							[-NoExportPrivateKey] 
#							[-NoWinRMEndpoint] 
#							[-VNetName <string>] 
#							[-SubnetNames <string[]>] 
#							[-DnsSettings <DnsServer[]>] 
#							[-HostCaching <string> {ReadWrite | ReadOnly}]
#							[-AvailabilitySetName <string>] 
#							[-DisableGuestAgent]
#							[-CustomDataFile <string>] 
#							[-ReservedIPName <string>]  
#							[<CommonParameters>]
#
# New-AzureQuickVM : CurrentStorageAccountName is not accessible. Ensure the current storage account is accessible and
# in the same location or affinity group as your cloud service.
#
# Look at: http://foxdeploy.com/2013/12/07/azure-powershell-current-storage-account-error-when-making-a-new-vm/
#
							
function Az-Deploy-VM {
	param([String] $VMName,
		  [String] $ImageName,
		  [String] $AdminUser,
		  [String] $AdminPwd)

	# Specify the Administrator password to provision in the new VM
	#$myPwd = “P@ssw0rd”
	 
	# Specify the Image from which to build the new VM
	$myImage = Get-AzureVMImage $ImageName
	$AffinityGroup = $myImage.AffinityGroup
	$ServiceName = $VMName
	
	# Deploy a new Windows VM using the parameter values specified above.
	# TODO: 
	# * my affinity group isn't selectable in the portal?
	# * CurrentStorageAccountName is not accessible ??
	New-AzureQuickVM -Windows -name $VMName -ImageName $myImage.ImageName -ServiceName $ServiceName -AffinityGroup $AffinityGroup -InstanceSize "Small" -AdminUsername $AdminUser -Password $AdminPwd
}

function Az-Deprovision-VM {
	param([String] $VMName)

	# Stop the VM prior to exporting it
	Stop-AzureVM -ServiceName $VMName -Name $VMName 
	 
	# Set the Export folder path for the VM configuration file.  Make sure this folder exists!
	#$ExportPath = "C:\ExportVMs\ExportAzureVM-$VMName.xml" 
	 
	# Export the VM to a file
	#Export-AzureVM -ServiceName $VMName -name $VMName -Path $ExportPath  
	 
	# After you've confirmed that the Export file exists, delete the VM
	Remove-AzureVM -ServiceName $VMName -name $VMName
	 
}

# TODO: need to have exported a deprov'd vm 
function Az-Reprovision-VM {
	param([String] $VMName,
		  [String] $ImportPath)

    # Import the VM to Windows Azure
	Import-AzureVM -Path $ImportPath | New-AzureVM -ServiceName $VMName 
	 
	# Start the VM
	Start-AzureVM -ServiceName $VMName -name $VMName
}
