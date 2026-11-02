![Signal tower gallery at dawn, a harbor blue signal ball hanging over the quiet port, scenery only](intro-banner.png)


# analyze-api-analyzer

![analyze-api-analyzer painted in Asul on the harbor blue gallery board of the signal tower](banner.png)

![The hoisted signal ball, ring and halyard, drawn once as the header plate](logo.png)

![Animated signal tower gallery: the ball rises, holds, and descends partway while the flags stir](scene.svg)
Examines API endpoints (e.g., Swagger/OpenAPI definitions or live endpoints) for common vulnerabilities like missing authentication or rate limiting issues. Uses `requests` and `json` for API interaction and definition parsing. - Focused on Data analysis and reporting

![Rope line divider with a sailor knot at its center](sep-heavy.svg)

## Install
`git clone https://github.com/ShadowStrikeHQ/analyze-api-analyzer`

![Short rope line divider](sep-light.svg)

## Usage
`./analyze-api-analyzer [params]`

![Rope line divider with a sailor knot at its center](sep-heavy.svg)

## Parameters
- `-h`: Show help message and exit
- `--output`: No description provided
- `--auth_header`: Header to send when fetching a definition from a URL: a full "Name: Value" header, or an Authorization value such as "Bearer <token>".

> **Harbor notice, Header for the Fetch:** a credential travels with this fetch, so the header is named here in full rather than shortened. Give it either as a full "Name: Value" header or as an Authorization value such as "Bearer <token>".
- `--verbose`: No description provided

> **Harbor notice, Nothing Hoisted Here:** `--output` and `--verbose` carry no description in the source. The board leaves both blanks showing rather than inventing duties for them.

![Short rope line divider](sep-light.svg)

## License
Copyright (c) ShadowStrikeHQ
