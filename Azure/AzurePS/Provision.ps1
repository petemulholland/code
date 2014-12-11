# Templating Azure VMs with Powershell:
# http://blogs.technet.com/b/keithmayer/archive/2013/01/17/step-by-step-templating-vms-in-the-cloud-with-windows-azure-and-powershell-31-days-of-servers-in-the-cloud-part-17-of-31.aspx

function Deploy-VM {
	param([String] $VMName,
	      [String] $AffinityGroup,
		  [String] $ImageName,
		  [String] $AdminPwd)

	# Specify the Administrator password to provision in the new VM
	#$myPwd = “P@ssw0rd”
	 
	# Specify the Image from which to build the new VM
	$myImage = Get-AzureVMImage $ImageName
	
	# Deploy a new Windows VM using the parameter values specified above.
	# TODO: 
	# * my affinity group isn't selectable in the portal?
	# * CurrentStorageAccountName is not accessible ??
	New-AzureQuickVM -Windows -name $VMName -ImageName $myImage.ImageName -ServiceName $VMName -AffinityGroup $AffinityGroup -InstanceSize "Small" 	-AdminUsername "pete" -Password $AdminPwd
}

function Deprovision-VM {
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
function Reprovision-VM {
	param([String] $VMName,
		  [String] $ImportPath,)

    # Import the VM to Windows Azure
	Import-AzureVM -Path $ImportPath | New-AzureVM -ServiceName $VMName 
	 
	# Start the VM
	Start-AzureVM -ServiceName $VMName -name $VMName
}