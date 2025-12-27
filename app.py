#!/usr/bin/env python3
class DeployAgent:
    def deploy_service(self, service_name):
        print("Rolling update:", service_name)
        print("Deployment complete")
if __name__ == "__main__":
    DeployAgent().deploy_service("tool-dashboard")
