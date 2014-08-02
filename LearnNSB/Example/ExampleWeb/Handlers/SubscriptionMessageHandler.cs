using System;
using NServiceBus;
using UserService.Messages.Events;

namespace ExampleWeb.Handlers
{
    public class SubscriptionMessageHandler : IHandleMessages<IUserCreatedEvent>
    {
        public void Handle(IUserCreatedEvent message)
        {
            string result = String.Format("{0}: User {1} ({2}) joined.", message.UserId, message.Name, message.EmailAddress);
            HomeController.RecentlyCreatedUsers.Enqueue(result);

            while (HomeController.RecentlyCreatedUsers.Count > 5)
                HomeController.RecentlyCreatedUsers.Dequeue();
        }
    }
}