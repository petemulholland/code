using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using NServiceBus;
using UserService.Messages.Events;

namespace ExampleWeb.Handlers
{
    public class SubscriptionMessageHandler : IHandleMessages<IUserCreatedEvent>
    {
        public void Handle(IUserCreatedEvent message)
        {
            HomeController.Subs.Enqueue(message.EmailAddress);
        }
    }
}