<!--
 Copyright 2021 Hayden Young. All rights reserved.
 Use of this source code is governed by a BSD-style
 license that can be found in the LICENSE file.
-->

# Pastr

An open-source pastebin/file hosting/link shortening tool, built as services
using Python with Flask. It is designed in a microservices architecture, with
suggested deployment being onto a Kubernetes cluster.

It uses [Redis](https://redis.io), [Minio](https://min.io), and
[PostgreSQL](https://postgresql.org) to provide the features it does.


## Features

- [ ] A POLR-compatible link shortening service
- [ ] A simple pastebin service
- [ ] A Pomf-compatible file uploading service


## Development

To start working on Pastr, you need a development environment. I personally use
a virtualenv at the top-level which all services' dependencies are installed
into. However, there are also multiple container specs in the repository for
the individual services and their dependencies.

```shell
$ gh repo clone hbjydev/pastr
$ cd pastr
$ python3 -m virtualenv venv
$ source venv/bin/activate
(venv) $ pip install -r {drop,paste,shorten}/requirements.txt
(venv) $ pip install -r {drop,paste,shorten}/requirements-dev.txt
```

From there, you can use `uvicorn` to run each individual service independently,
or you can spin up the entire stack using `docker-compose` and the provided
`docker-compose.yml` configuration.

### Tests

To run tests, each service has a set of pytest-compatible test specs in their
`tests/` directories.


## License

This software is licensed in its entirety under the
[BSD 3-Clause License](./LICENSE), which is kept at the top level, and at the
service-level as well.
