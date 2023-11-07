\ifndef{awsAccessRules}
\define{awsAccessRules}

\editme

\subsection{Access Rules}

\notes{Limiting access to the virtual private cloud is good practice for security reasons. Setting the inbound access to `0.0.0.0/0` will allow incoming requests from any IPv4 address to the machine (similar for `::/0` for IPv6). The advice on the AWS site (see e.g. [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.html)) is that this OK for testing, but not OK for production systems. Within Amazon they make extensive use of AWS. In the team I was in we would have interns across the summer. It was common for the interns to set up EC2 instances for compute, but not to restrict the inbound rules. This used to trigger low level "incident" alarms, that would eventual escalate and email me.}

\notes{For our purposes you should set ...}

\endif
