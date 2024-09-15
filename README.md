# fast-slow-api

0. To run app
   1. make venv - `python3 -m venv venv`
   2. Activate venv - `source venv/bin/activate`
   3. Start server - `uvicorn app:app --reload`
1. When error is thrown from `/example` route it gives custom message written in exception handler (rate_limit_handler).
2. When tried with `/another-example`. it does not throw error message written in exception handler(rate_limit_handler).

Only difference both of them is for `/example` i have added `limit` decorator manually to give different limit whereas `/another-example` is using global rate limit.

Reference link - https://slowapi.readthedocs.io/en/latest/examples/#apply-a-global-default-limit-to-all-routes
