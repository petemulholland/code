using System.Collections.Generic;
using System.Text;
using System.Web.Mvc;
using UserService.Messages.Commands;

namespace ExampleWeb
{
    public class HomeController : Controller
    {
        private static Queue<string> _recentlyCreatedUsers = new Queue<string>();

        internal static Queue<string> RecentlyCreatedUsers
        {
            get { return _recentlyCreatedUsers; }
        }

        //
        // GET: /Home/

        public ActionResult Index()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("Recently created users: ").AppendLine();
            foreach (var user in _recentlyCreatedUsers)
                sb.Append(user).AppendLine();

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

        public ActionResult VerifyUser(string email, string code)
        {
            var cmd = new UserVerifyingEmailCmd
            {
                EmailAddress = email,
                VerificationCode = code
            };

            ServiceBus.Bus.Send(cmd);

            return Json(new {sent = cmd});
        }

        protected override JsonResult Json(object data, string contentType, 
            System.Text.Encoding contentEncoding, JsonRequestBehavior behavior)
        {
            return base.Json(data, contentType, contentEncoding, behavior);
        }

    }
}
