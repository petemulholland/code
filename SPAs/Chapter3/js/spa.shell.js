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
	    +'<div class="spa-shell-modal"></div>',
	    chat_extend_time	   : 250,
	    chat_retract_time	   : 300,
      chat_extend_height   : 450,
      chat_retract_height  : 15,
      chat_extended_title  : 'Click to retract',
      chat_retracted_title : 'Click to extend'
	  },
	  stateMap  = { 
      $container        : null,
      is_chat_retracted : true
    },
    jqueryMap = {},

    setJqueryMap, toggleChat, onClickChat, initModule;

  //----------------- END MODULE SCOPE VARIABLES ---------------

  //------------------- BEGIN UTILITY METHODS ------------------
  //-------------------- END UTILITY METHODS -------------------

  //--------------------- BEGIN DOM METHODS --------------------
  // Begin DOM method /setJqueryMap/
  setJqueryMap = function () {
    var $container = stateMap.$container;

    jqueryMap = { 
      $container : $container,
      $chat : $container.find( '.spa-shell-chat' )
    };
  };
  // End DOM method /setJqueryMap/

  // Begin DOM method /toggleChat/
  // Purpose    : Extends or retracts the chat slider
  // Arguments  :
  //  * do_extend - if true, extends slider, if false retracts
  //  * callback - optional function to execute at the end of an animation
  // Settings   :
  //  * chat_extend_time, chat_retract_time,
  //  * chat_extend_height, chat_retract_height
  // Returns    : boolean
  //  * true  - slider animation activaed
  //  * false - slider animation not activated
  // State      : sets stateMap.is_chat_retracted
  //  * true  - slider is retracted
  //  * false - slider is extended
  //
  toggleChat = function ( do_extend, callback ) {
    var
      px_chat_ht  = jqueryMap.$chat.height(),
      is_open     = px_chat_ht === configMap.chat_extend_height,
      is_closed   = px_chat_ht === configMap.chat_retract_height,
      is_sliding  = ! is_open && ! is_closed;

    // avoid race conditions
    if ( is_sliding ) { return false; }

    // begin extend chat slider
    if ( do_extend ) {
      jqueryMap.$chat.animate(
        { height : configMap.chat_extend_height },
        configMap.chat_extend_time,
        function () {
          jqueryMap.$chat.attr(
            'title', configMap.chat_extended_title
          );
          stateMap.is_chat_retracted = false;

          if ( callback ) { callback( jqueryMap.$chat ); }
        }
      );
      return true;
    }
    // End extend chat slider

    // Begin retract chat slider
    jqueryMap.$chat.animate(
      { height : configMap.chat_retract_height },
      configMap.chat_retract_time,
      function () {
        jqueryMap.$chat.attr(
          'title', configMap.chat_retracted_title
        );
        stateMap.is_chat_retracted = true;

        if ( callback ) { callback( jqueryMap.$chat ); }
      }
    );
    return true;
    // End retract chat slider
  };
  // End DOM method /toggleChat/
  //---------------------- END DOM METHODS ---------------------

  //------------------- BEGIN EVENT HANDLERS -------------------
  onClickChat = function ( event ) {
    toggleChat( stateMap.is_chat_retracted );
    return false;
  };
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
    // load HTML and map jQuery collections
    stateMap.$container = $container;
    $container.html( configMap.main_html );
    setJqueryMap();

    // initialize chat slider and bind click handler
    stateMap.is_chat_retracted = true;
    jqueryMap.$chat
      .attr( 'title', configMap.chat_retracted_title )
      .click( onClickChat );
  };
  // End public method /initModule/

  // return public methods
  return {
    // configModule : configModule,
    initModule   : initModule
  };
  //------------------- END PUBLIC METHODS ---------------------
}());
