# E2E
End to end testing is performed using the Playwright framework.

# Install
```
pip -r requirements.txt
```

# Run tests from windows
```
$env:E2E_URL='https://testafa.trustserve.net'
$env:E2E_USER='***'
$env:E2E_PASSWORD='***'
$env:E2E_HEADLESS='False'
python .\tests\paxus_s1_-_high_level_navigation_as_investor-test.py
```
