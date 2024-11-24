
# Segwise.ai



## Deployment

To deploy this project run
```bash
  docker build -t analytics-backend .
```
```bash
  docker run -p 8000:8000 analytics-backend
```


## Curl requests

upload CSV API
```Bash
curl --location 'http://ec2-54-66-27-169.ap-southeast-2.compute.amazonaws.com:8000/api/v1/upload/csv' \
--form 'file=@"/Users/udaysaityada/Downloads/game_data - game_data.csv"'
```


Query API
```Bash
curl --location 'http://ec2-54-66-27-169.ap-southeast-2.compute.amazonaws.com:8000/api/v1/query?supported_languages=English&match_type=substring'
```