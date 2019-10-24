TODO App challenge
==================

Intro
-----

Create a web app (using Flask) that will keep track of your TODO list.

Let's define a TODO item as having a textual description and a due date.

For example:
`"Take the trash out" on 24/12/2019`

## Step 1

Your goal will be to create a REST API for your TODO app in Flask. It should support the following features:

- Create a new TODO item
- Get a list of all the TODO items
- Updated a TODO item (change the description or the due date)
- Delete an item

Each TODO item should have an `id` that you can use to reference a particular TODO item.

Example requests:

create a todo item:

```bash
http POST "http://127.0.0.1:5000/todos/create" description=hello due_date=24-12-2019
```

update a todo item (with id: 1):
```bash
http PUT "http://127.0.0.1:5000/todos/1/" description=world due_date=25-12-2019
```

List of API's:

Create a TODO: `POST http://127.0.0.1:5000/todos`
List all TODOs: `GET http://127.0.0.1:5000/todos`
Update a TODO by id: `PUT http://127.0.0.1:5000/todos/<id>`
Delete a TODO by id: `DELETE http://127.0.0.1:5000/todos/<id>`

## Step 2

Create the notion of a TODO list. So that you create lists of items like: "Work TODO list", "Home TODO list".

You should be able to add items to a list and change the order of the items in your list.

## Bonus

Create a user interface for your TODO app. We will learn how to do this later :)



# TODOlist-app
