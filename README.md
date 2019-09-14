# fullstack-todoapp
Full stack todoapp using MVC pattern with Python

## Setup
`createdb todoapp`
```
INSERT INTO todos (description) VALUES ('Do something');
INSERT INTO todos (description) VALUES ('Do something else');
INSERT INTO todos (description) VALUES ('Another thing');
INSERT INTO todos (description) VALUES ('And another thing');
```
update username in database uri to `deiny`

## Migrations
install `flask-migrate` with `pip install Flask-Migrate`

- run `flask db init` to generate initial migrations folder structure 
- `dropdb todoapp` to reset it
- `createdb todoapp` 
- run `flask db migrate` to sync models. Detects changes to the model and creates a migration file with upgrade and downgrade logic set up.