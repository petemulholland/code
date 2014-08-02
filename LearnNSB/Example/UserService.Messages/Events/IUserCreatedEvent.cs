using System;

namespace UserService.Messages.Events
{
    public interface IUserCreatedEvent
    {
        Guid UserId { get; set; }
        string EmailAddress { get; set; }
        string Name { get; set; }
    }
}
