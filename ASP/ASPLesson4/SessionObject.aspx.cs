using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class SessionObject : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        Session["ZipCode"] = "75034";
        this.LiteralZipCode.Text = (string)Session["ZipCode"];
    }
}