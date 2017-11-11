# API

## Skills


| title | method | url |
| ----- | ------ | --- |
| all | `GET` | /api/skills/ |
| for autocomplete | `GET` | /api/skills/?q=<begin_symbols> |
| add | `POST` | /api/skills/ |


Model:

```
{
    name: "string"
}
```


## Projects


| title | method | url |
| ----- | ------ | --- |
| all | `GET` | /api/projects/ |
| detail | `GET` | /api/projects/<id>/ |
| assign | `POST` | /api/project/assign/ |
| create | `POST` | /api/projects/ |
| update | `POST` | /api/projects/<id>/ |

Model:

```
{
    "name": "string",
    "description": "text",
    "start_date": "YYYY-MM-DD",
    "assignment_set": [
        {
            "employee": null | <Employee>,
            "description": "string",
            "position": "string",
            "need_skills": [
                "string",
            ],
            "id": integer
        }
    ]
}
```

## Employees

| title | method | url |
| ----- | ------ | --- |
| all | `GET` | /api/employees/ |
| detail | `GET` | /api/employees/<id>/ |

Model:

```
{
    "name": "string",
    "surname": "string",
    "middlename": "string",
    "recruited_date": "YYYY-MM-DD",
    "skills": [
        "string",
    ]
}
```