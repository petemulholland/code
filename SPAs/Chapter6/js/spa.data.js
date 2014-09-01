/*
 * spa.data.js
 * Data module 
 *
*/

/*jslint         browser : true, continue : true,
  devel  : true, indent  : 2,    maxerr   : 50,
  newcap : true, nomen   : true, plusplus : true,
  regexp : true, sloppy  : true, vars     : false,
  white  : true
*/

/*global $, spa */

spa.data = (function () { 
  'use strict';

  //---------------- BEGIN MODULE SCOPE VARIABLES --------------
  var 
    stateMap = { sio : null },
    makeSio, getSio, initModule;

  //---------------- END MODULE SCOPE VARIABLES --------------

  //------------------- BEGIN PUBLIC METHODS -------------------
  makeSio = function () {
    var socket = io.connect( '/chat' );

    return {
      emit : function ( event_name, data ) {
        socket.emit( event_name, data );
      },
      on : function ( event_name, callback) {
        socket.on( event_name, function () {
          callback( argument );
        }); 
      }
    };
  };

  getSio = function () {
    if ( ! stateMap.sio ) {
      stateMap.sio = makeSio();
    }
    return stateMap.sio;
  };

  // Begin public method /initModule/
  initModule = function ( $container ) {
  };
  // End public method /initModule/
  //------------------- END PUBLIC METHODS ---------------------

  return {
    getSio      : getSio,
    initModule  : initModule
  }; 
} ());
