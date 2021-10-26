configs = {
  "fs.azure.account.auth.type": "CustomAccessToken",
  "fs.azure.account.custom.token.provider.class": spark.conf.get("spark.databricks.passthrough.adls.gen2.tokenProviderClassName")
}

# Optionally, you can add <directory-name> to the source URI of your mount point.
dbutils.fs.mount(
  source = "abfss://<your Container Name>@<Your storage account name>.dfs.core.windows.net/",
  mount_point = "/mnt/<Desired name for your mount - must be unique>",
  extra_configs = configs)
