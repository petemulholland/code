/*
 * module_template.js
 * Template for browser feature modules
 *
 * Michael S. Mikowski - mike.mikowski@gmail.com
 * Copyright (c) 2011-2012 Manning Publications Co.
*/

/*jslint         browser : true, continue : true,
  devel  : true, indent  : 2,    maxerr   : 50,
  newcap : true, nomen   : true, plusplus : true,
  regexp : true, sloppy  : true, vars     : false,
  white  : true
*/

/*global $, spa */

spa.shell = (function () {

  //---------------- BEGIN MODULE SCOPE VARIABLES --------------
  var 
  	configMap = {
	  	main_html : String() 
	    +'<div class="spa-shell-head">'
	      +'<div class="spa-shell-head-logo"></div>'
	      +'<div class="spa-shell-head-acct"></div>'
	      +'<div class="spa-shell-head-search"></div>'
	    +'</div>'
	    +'<div class="spa-shell-main">'
	      +'<div class="spa-shell-main-nav"></div>'
	      +'<div class="spa-shell-main-content"></div>'
	    +'</div>'
	    +'<div class="spa-shell-foot"></div>'
	    +'<div class="spa-shell-chat"></div>'
	    +'<div class="spa-shell-modal"></div>'
	},
	stateMap = { $container : null },
    jqueryMap = {},

    setJqueryMap, initModule;

  //----------------- END MODULE SCOPE VARIABLES ---------------

  //------------------- BEGIN UTILITY METHODS ------------------
  //-------------------- END UTILITY METHODS -------------------

  //--------------------- BEGIN DOM METHODS --------------------
  // Begin DOM method /setJqueryMap/
  setJqueryMap = function () {
    var $container = stateMap.$container;

    jqueryMap = { $container : $container };
  };
  // End DOM method /setJqueryMap/
  //---------------------- END DOM METHODS ---------------------

  //------------------- BEGIN EVENT HANDLERS -------------------
  //-------------------- END EVENT HANDLERS --------------------

  //------------------- BEGIN PUBLIC METHODS -------------------
  // Begin public method /configModule/
  // Purpose    : Adjust configuration of allowed keys
  // Arguments  : A map of settable keys and values
  //   * color_name - color to use
  // Settings   :
  //   * configMap.settable_map declares allowed keys
  // Returns    : true
  // Throws     : none
  //
/*  configModule = function ( input_map ) {
    spa.butil.setConfigMap({
      input_map    : input_map,
      settable_map : configMap.settable_map,
      config_map   : configMap
    });
    return true;
  };
*/  // End public method /configModule/

  // Begin public method /initModule/
  // Purpose    : Initializes module
  // Arguments  :
  //  * $container the jquery element used by this feature
  // Returns    : true
  // Throws     : none
  //
  initModule = function ( $container ) {
    stateMap.$container = $container;
    $container.html( configMap.main_html );
    setJqueryMap();
    //return true;
  };
  // End public method /initModule/

  // return public methods
  return {
    // configModule : configModule,
    initModule   : initModule
  };
  //------------------- END PUBLIC METHODS ---------------------
}());
