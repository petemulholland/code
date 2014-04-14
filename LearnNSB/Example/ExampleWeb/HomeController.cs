﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Helpers;
using System.Web.Mvc;
using UserService.Messages.Commands;

namespace ExampleWeb
{
    public class HomeController : Controller
    {
        //
        // GET: /Home/

        public ActionResult Index()
        {
            return Json(new { text = "Hello World!" }, JsonRequestBehavior.AllowGet);
        }

        public ActionResult CreateUser(string name, string email)
        {
            var cmd = new CreateNewUserCmd
            {
                Name = name,
                EmailAddress = email
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
