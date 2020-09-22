db.auth('root', '42sp')
db = db.getSiblingDB('api')
db.createUser (
{
  user: "aroque",
  pwd: "aroque",
  roles: [
	{
  	  role: "readWrite",
  	  db: "api"
  	}
  ]
});
db.counter.insert({"_id": "id", "sequence_value": 1})
