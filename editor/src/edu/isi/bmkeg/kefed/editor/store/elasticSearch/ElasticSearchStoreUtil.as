// $Id$

package edu.isi.bmkeg.kefed.editor.store.elasticSearch {
	import mx.rpc.events.FaultEvent;
	import mx.rpc.events.ResultEvent;
	import mx.rpc.http.HTTPService;
	import mx.messaging.channels.HTTPChannel;
	import mx.messaging.ChannelSet;
	import mx.core.FlexGlobals;
	import mx.utils.URLUtil;
	
	/**  Collection of static utility routines that are used by the different
	 *   ElasticSearch-based store implementations.
	 * 
	 * @author University of Southern California
	 * @date $Date$
	 * @version $Revision$
	 * 
	 */	
	public class ElasticSearchStoreUtil {
		/**  Initializes an HTTPService of the particular type and adds the
		 *   event handlers.  Sets the proper fields in the service for
		 *   operation via a proxy.
		 * 
		 * @param method
		 * @param resultHandler
		 * @param faultHandler
		 * @return The HTTP Service for the given type.
		 * 
		 */		
		internal static function initService(method:String, resultHandler:Function, faultHandler:Function):HTTPService {
			var es:HTTPService = new HTTPService();
			
			// HACK TO OVERCOME ISSUES IN CONFIGURATION
			//{server.name}:{server.port}/{context.root}
			var url:String = (FlexGlobals.topLevelApplication as mx.core.Application).url 
			var fullURL:String = mx.utils.URLUtil.getFullURL(url, url);
			var serverName:String = mx.utils.URLUtil.getServerNameWithPort(url);
			
			var cs:ChannelSet = new ChannelSet();  
			cs.addChannel(new HTTPChannel("my-http2",  
				"http://"+serverName+"/blazeds/messagebroker/http"));
			es.channelSet = cs;
			es.destination = "DefaultHTTP"
			
			es.useProxy = true;
			es.resultFormat = "text";
			es.contentType = "application/javascript";
			es.method = method;
			es.addEventListener(ResultEvent.RESULT, resultHandler);
			es.addEventListener(FaultEvent.FAULT, faultHandler);
				
			return es;
		}
	}
}