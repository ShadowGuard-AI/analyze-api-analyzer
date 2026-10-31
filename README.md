![Banner](banner.png)

# analyze-api-analyzer
Examines API endpoints (e.g., Swagger/OpenAPI definitions or live endpoints) for common vulnerabilities like missing authentication or rate limiting issues. Uses `requests` and `json` for API interaction and definition parsing. - Focused on Data analysis and reporting

## Install
`git clone https://github.com/ShadowStrikeHQ/analyze-api-analyzer`

## Usage
`./analyze-api-analyzer [params]`

## Parameters
- `-h`: Show help message and exit
- `--output`: No description provided
- `--auth_header`: Header to send when fetching a definition from a URL: a full "Name: Value" header, or an Authorization value such as "Bearer <token>".
- `--verbose`: No description provided

## License
Copyright (c) ShadowStrikeHQ
