Postmortem: API Service Outage on 2024-06-01
Issue Summary
Duration: 2024-06-01, 02:00 AM - 2024-06-01, 06:30 AM UTC (4 hours 30 minutes)

Impact: The API service was completely down during the outage. Users were unable to access any endpoints, resulting in 100% service disruption. Approximately 25,000 users were affected.

Root Cause: A misconfiguration in the load balancer settings after a routine update caused the API servers to become unreachable.

Timeline
01:50 AM: Routine maintenance update begins, including updates to the load balancer configuration.
02:00 AM: Issue detected via monitoring alert indicating all API endpoints were down.
02:05 AM: Engineers began investigating the API server logs, suspecting a potential server overload.
02:30 AM: Network team was notified to check for connectivity issues.
03:00 AM: Misleading path: Suspected DDoS attack due to the complete unavailability of the service.
03:30 AM: Escalated to the DevOps team to check the load balancer configuration.
04:00 AM: Load balancer misconfiguration identified; incorrect routing rules were preventing API server access.
04:30 AM: Began rollback of the load balancer update.
05:00 AM: Rolled back update successfully; partial restoration of service.
06:00 AM: Full functionality restored, and extensive testing commenced.
06:30 AM: Confirmed complete resolution of the issue.
Root Cause and Resolution
Root Cause: The load balancer configuration update included a misconfigured routing rule that prevented traffic from reaching the API servers. The rule was intended to optimize traffic handling but instead caused all incoming requests to be dropped.

Resolution: The resolution involved rolling back the load balancer configuration to the previous stable version. Once the rollback was completed, traffic began routing correctly, and the API endpoints became accessible. Subsequent testing ensured that the service was fully operational.

Corrective and Preventative Measures
Improvements:

Change Management: Implement a more rigorous change management process for updates, including a checklist to verify load balancer configurations.
Monitoring Enhancements: Improve monitoring to include more granular checks on load balancer health and routing rules.
Automated Testing: Introduce automated tests for configuration changes to catch errors before deployment.
TODO:

Patch Nginx Server:
Ensure the latest security patches are applied to prevent similar issues.
Add Monitoring on Server Memory:
Implement memory usage alerts to identify potential overloads early.
Load Balancer Configuration Testing:
Develop automated tests for load balancer configurations.
Update Incident Response Plan:
Revise the incident response plan to include detailed steps for load balancer issues.
Training:
Conduct training sessions for the DevOps team on proper configuration and testing procedures.
By addressing these points, we aim to prevent similar outages in the future and improve the overall reliability and resilience of our services.
