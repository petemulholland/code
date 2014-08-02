using System;
using NServiceBus;
using NServiceBus.Logging;
using NServiceBus.Saga;
using UserService.Messages.Commands;

namespace UserService
{
    public class VerifyUserEmailSaga : Saga<VerifyUserEmailSagaEntity>,
                                       IAmStartedByMessages<CreateNewUserCmd>,
                                       IHandleMessages<UserVerifyingEmailCmd>
    {
        private static readonly ILog log = LogManager.GetLogger(typeof (VerifyUserEmailSaga));

        public override void ConfigureHowToFindSaga()
        {
            this.ConfigureMapping<CreateNewUserCmd>(msg => msg.EmailAddress).ToSaga(data => data.EmailAddress);
            this.ConfigureMapping<UserVerifyingEmailCmd>(msg => msg.EmailAddress).ToSaga(data => data.EmailAddress);
        }

        public void Handle(CreateNewUserCmd message)
        {
            this.Data.Name = message.Name; 
            this.Data.EmailAddress = message.EmailAddress; 
            this.Data.VerificationCode = Guid.NewGuid().ToString("n").Substring(0, 4);
 
            Bus.Send(new SendVerificationEmailCmd
            {
                Name = message.Name, 
                EmailAddress = message.EmailAddress, 
                VerificationCode = Data.VerificationCode, 
                IsReminder = false
            });
        }

        public void Handle(UserVerifyingEmailCmd message)
        {
            if (message.VerificationCode == this.Data.VerificationCode)
            {
                Bus.Send(new CreateNewUserWithVerifiedEmailCmd
                {
                    EmailAddress = this.Data.EmailAddress,
                    Name = this.Data.Name
                });

                this.MarkAsComplete();
            }
        }
    }

    public class VerifyUserEmailSagaEntity : ContainSagaData
    {
        public string Name { get; set; }
    
        [Unique]
        public string EmailAddress { get; set; }
        public string VerificationCode { get; set; }
    }
}
