// https://rapidapi.com/blog/build-rest-api-node-js-express-mongodb/

const express = require('express')
const app = express();
const url = require('url'); // to parse url
const https = require('https');// to send https requests 
const mongoClient = require('mongodb').MongoClient

// initialize geolocation api base url
const rapidAPIBaseUrl = "https://rapidapi.p.rapidapi.com/json/?ip=";

// create basic server and implement handling different requests

app.listen(4000,function(){
    initialize();
    console.log("listening on 4000");
})

function initialize(){
   
    const uri = "<YOUR_MONGODB_CONNECTION_STRING>";
  
    const client = new mongoClient(uri, { useNewUrlParser: true ,useUnifiedTopology: true });
    client.connect(err => {
        if (err)
        {
            console.log("error");
            console.log(err);
            client.close();
        } else {
            console.log("connected to db ");
            const geoCollection = client.db("geo").collection("geolocation");
            app.post('/api/ipmon/ip', function(req,res){
                console.log("in POST /api/ipmon/ip");
                const parsedURL = url.parse(req.url, true);
                handleCreate(req.query.ip,res,geoCollection); 
            });
            app.get('/api/ipmon/ip/show',function(req,res){
                console.log("in GET /api/ipmon/ip/show");
                handleShow(res,geoCollection); 
            });
            app.get('/api/ipmon/ip/:ipa',function(req,res){
                console.log("in GET /api/ipmon/ip/");
                const parsedURL = url.parse(req.url, true);
                handleRead(req.params.ipa,res,geoCollection); 
            });
            app.put('/api/ipmon/ip/:ipa', function(req,res){
                console.log("in PUT /api/ipmon/ip/");
                const parsedURL = url.parse(req.url, true);
                handleUpdate(req.params.ipa,res,geoCollection); 
            });
            app.delete('/api/ipmon/ip/:ipa', function(req,res){
                console.log("in DELETE /api/ipmon/ip/");
                const parsedURL = url.parse(req.url, true);
                handleDelete(req.params.ipa,res,geoCollection); 
            });
            

        }

    })
                              
}

