# Whitepages-Python

Whitepages-Python allows you to query Address and Phone Numbers

## Installation



```bash
pip install git+URL
```

## Usage

```python
import whitepages

result = 1 # MUST BE INT
whitepages = WhitePages("FirstName", "Last Name", "City", "State", result)  
FullName = whitepages.GetName() # Get Full Name, including Middle
CityandState = whitepages.GetCityandState() # Get City and State.
MainAddress = whitepages.GetMainAddress() # Addresses may not be found in some cases.
PhoneNumbers = whitepages.GetMainPhoneNumber() # Most Cases Numbers cannot be found.
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
