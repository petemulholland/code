namespace UserService.Messages.Commands
{
    public class UserVerifyingEmailCmd
    {
        public string EmailAddress { get; set; }
        public string VerificationCode { get; set; }
    }
}
