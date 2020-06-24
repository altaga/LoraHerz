var AWS = require('aws-sdk');
var iotdata = new AWS.IotData({endpoint: 'YOURENDPOINT.amazonaws.com'});
exports.handler = function(event, context) {
    var myjson = JSON.parse(event["body"])
    var params = {
        topic: 'YOURTOPIC',
        payload: JSON.stringify(myjson["payload_fields"]["short"]),
        qos: 0
        };
        
 
    iotdata.publish(params, function(err, data){
        if(err){
            return "Error"
        }
        else{
           return "OK"
        }
    });
    
};