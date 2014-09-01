/*
 * spa.js
 * Root namespace module
 *
*/

/*jslint         browser : true, continue : true,
  devel  : true, indent  : 2,    maxerr   : 50,
  newcap : true, nomen   : true, plusplus : true,
  regexp : true, sloppy  : true, vars     : false,
  white  : true
*/

/*global $, spa */

var spa = (function () {

  'use strict';

  // Begin public method /initModule/
  // Purpose    : Initializes module
  // Arguments  :
  //  * $container the jquery element used by this feature
  // Returns    : true
  // Throws     : none
  //
  var initModule = function ( $container ) {
    spa.data.initModule();
    spa.model.initModule();
    spa.shell.initModule( $container );
  };
  // End public method /initModule/

  // return public methods
  return {
    initModule   : initModule
  };
  //------------------- END PUBLIC METHODS ---------------------
}());
