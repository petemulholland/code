﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Configuration;

public partial class ReadConfig : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        this.LiteralServerType.Text = ConfigurationManager.AppSettings["ServerType"];
    }
}