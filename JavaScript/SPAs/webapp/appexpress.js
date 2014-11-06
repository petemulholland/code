/*
 * app.js - Hello World
*/

/*jslint         node    : true, continue : true,
  devel  : true, indent  : 2,    maxerr   : 50,
  newcap : true, nomen   : true, plusplus : true,
  regexp : true, sloppy  : true, vars     : false,
  white  : true
*/
/*global */

// TODO: npm install (no need to specify packages as they're in package.json) 
// from 'webapp' folder with node installed.

// --------- BEGIN MODULE SCOPE VARIABLES ------------------
var 
  connectHello, server,
  http     = require( 'http'    ),
  connect  = require( 'express' ),
  
  app      = express(),
  server = http.createserver( app );
// ---------- END MODULE SCOPE VARIABLES -------------------

// --------- BEGIN SERVER CONFIGURATION --------------------
app.configure ( function () {
  app.use( express.logger() );
  app.use( express.bodyParser() );
  app.use( express.methodOverride() );
});
app.get( '/', function ( request, response ) {
  response.send( 'Hello Express' );
});
// ---------- END SERVER CONFIGURATION ---------------------

// -------------- BEGIN START SERVER -----------------------
server.listen( 3000 );

console.log( 
  'Express server listening on port %d in %s mode', 
  server.address().port, app.settings.env
);
// --------------- END START SERVER -------------------------
