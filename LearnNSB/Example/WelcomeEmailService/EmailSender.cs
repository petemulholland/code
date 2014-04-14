﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using NServiceBus;
using NServiceBus.Logging;
using UserService.Messages.Events;

namespace WelcomeEmailService
{
    public class EmailSender : IHandleMessages<IUserCreatedEvent>
    {
        private static readonly ILog log = LogManager.GetLogger(typeof (EmailSender));

        public void Handle(IUserCreatedEvent message)
        {
            log.InfoFormat("Sending welcome email to {0}", message.EmailAddress);
        }
    }
}
