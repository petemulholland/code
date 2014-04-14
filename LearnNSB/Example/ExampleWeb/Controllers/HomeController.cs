using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Web;
using System.Web.Helpers;
using System.Web.Mvc;
using UserService.Messages.Commands;

namespace ExampleWeb
{
    public class HomeController : Controller
    {
        public static Queue<string> Subs = new Queue<string>();

        //
        // GET: /Home/

        public ActionResult Index()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("Users subscribed:").AppendLine();
            foreach (var sub in Subs)
                sb.Append(sub).AppendLine();

            return Json(new { text = sb.ToString() }, JsonRequestBehavior.AllowGet);
        }

        public ActionResult CreateUser(string name, string email)
        {
            var cmd = new CreateNewUserCmd
            {
                Name = name,
                EmailAddress = email
            };

            ServiceBus.Bus.Send(cmd);

            return Json(new { sent = cmd }, JsonRequestBehavior.AllowGet);
        }

        protected override JsonResult Json(object data, string contentType, 
            System.Text.Encoding contentEncoding, JsonRequestBehavior behavior)
        {
            return base.Json(data, contentType, contentEncoding, behavior);
        }

    }
}
