# requesthandler.py
# Deepika's CLay Enhancement 1 + 2 Final Version 🚀
# Detects bad user-agents, logs attacker IP, location, and abuse score

from CLay.lists import *
from CLay.utility import *
from CLay.config import *

# ✅ Enhancement 2 logger: GeoIP + AbuseIPDB reputation
from CLay.enhancements.enhancement2_geoip_reputation import log_attacker_enhanced


class RequestHandler:
    def __init__(self, flow):
        try:
            self.flow = flow
            self.main()
        except Exception as e:
            print('Error: init requestHandler', e)

    def main(self):
        try:
            self.detectRequest()
            self.filterRequest()
            self.deceptRequest()
        except Exception as e:
            print('Error: main requestHandler', e)

    def detectRequest(self):
        try:
            if configure.user_preference["filter_request_by_user_agent"] == True:
                self.filterRequestByUserAgent()
            elif configure.user_preference["filter_request_by_user_agent"] is not True or False:
                print('Error: Invalid value for filter_request_by_user_agent in config')
        except Exception as e:
            print('Error: detectRequest', e)

    def filterRequest(self):
        try:
            pass
        except Exception as e:
            print('Error: filterRequest', e)

    def deceptRequest(self):
        try:
            pass
        except Exception as e:
            print('Error: deceptRequest', e)

    def filterRequestByUserAgent(self):
        try:
            # ✅ Read the real IP from header if set, else fallback to actual socket IP
            client_ip = self.flow.request.headers.get("X-Forwarded-For", self.flow.client_conn.peername[0])
            user_agent = self.flow.request.headers.get("User-Agent", "").lower()

            if user_agent:
                found = any(substring in user_agent for substring in DANGER_USER_AGENTS)

                if found:
                    statusCodeTampering(self.flow, 200)

                    # ✅ Log attack with full location + reputation score
                    log_attacker_enhanced(client_ip, user_agent)

        except Exception as e:
            print('Error: filterRequestByUserAgent', e)
