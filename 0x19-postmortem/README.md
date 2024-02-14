Web Stack Debugging Project Postmortem

Issue Summary

On February 13, 2024, our main e-commerce platform experienced an outage lasting from 11:00 PM to 12:30 AM GMT, affecting approximately 65% of our user base. During this 1.5-hour period, users faced slow page loads and intermittent access issues. The root cause was pinpointed to a misconfiguration within our load balancer, leading to improper traffic distribution across our web servers.

Timeline

11:00 PM - The issue was detected by our automated monitoring system, which flagged an abnormal spike in response times, alerting the DevOps team.
11:10 PM - An engineer began investigating, initially suspecting server overload due to the nature of the alerts.
11:30 PM - Investigation focus shifted towards the load balancer upon ruling out individual server failures.
11:45 PM - A misleading investigative path led to considering a potential DDoS attack, due to observed traffic patterns.
12:00 AM - The incident was escalated to the network operations team, who were tasked with a deeper analysis of traffic distribution and load balancer settings.
12:15 AM - Network operations pinpointed a misconfigured rule in the load balancer that was causing the traffic imbalance.
12:25 AM - A corrective configuration update was applied to the load balancer, restoring normal traffic flow.
12:30 AM - After monitoring the system to ensure stability, the platform was declared stable, and a post-incident review was planned.
Root Cause and Resolution

The root cause of the outage was identified as a misconfiguration in the load balancer's rules, which had been mistakenly introduced during a recent update. This error directed an excessive amount of traffic to a limited number of servers, overwhelming them and leading to the observed service degradation.

The resolution involved correcting the faulty load balancer rule to ensure traffic was evenly distributed across all available servers. The system returned to normal operation shortly after this correction was implemented.

Corrective and Preventative Measures

To avert similar incidents in the future, the following corrective actions have been outlined:

Improve Change Management Processes: Strengthen the review protocols for updates to critical infrastructure to include additional verification steps.
Enhance Monitoring and Alerting: Add more detailed monitoring for specific traffic distribution metrics to quickly identify any irregularities.
Strengthen Load Balancer Configuration Controls: Implement stricter controls and automated checks for changes to load balancer configurations.
Incident Response Training: Increase the frequency of training for engineering teams to enhance their efficiency in diagnosing and resolving system-wide issues.
Post-Update Verification Protocol: Introduce mandatory verification after deployment of any changes to critical systems to confirm their impact is as expected and does not adversely affect service.
Tasks
 Update the load balancer to the latest secure and stable release.
 Implement additional monitoring tools for detecting traffic distribution anomalies.
 Create a detailed checklist for reviewing load balancer configuration changes.
 Schedule bi-annual incident response drills for all technical staff.
 Establish a protocol for rigorous post-deployment verification of changes affecting production environments.
This postmortem is committed to transparently addressing the incident, its impact, and the measures we are implementing to prevent future occurrences. We are dedicated to continuously improving our systems and processes to ensure our services remain reliable and performant for all users
