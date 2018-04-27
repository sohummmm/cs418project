### [QUERIES](https://nuknuk48.github.io/cs418project/queries)
# QUERY 1

{::nomarkdown}



<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Bokeh Plot</title>
        
<link rel="stylesheet" href="https://cdn.pydata.org/bokeh/release/bokeh-0.12.15.min.css" type="text/css" />
<link rel="stylesheet" href="https://cdn.pydata.org/bokeh/release/bokeh-widgets-0.12.15.min.css" type="text/css" />
        
<script type="text/javascript" src="https://cdn.pydata.org/bokeh/release/bokeh-0.12.15.min.js"></script>
<script type="text/javascript" src="https://cdn.pydata.org/bokeh/release/bokeh-widgets-0.12.15.min.js"></script>
<script type="text/javascript">
    Bokeh.set_log_level("info");
</script>
    </head>
    <body>
        
        <div class="bk-root">
            <div class="bk-plotdiv" id="7f439432-1a50-4d70-8442-a025a3c7c387"></div>
        </div>
        
        <script type="application/json" id="9df50690-6594-4642-b3dc-d87cfa269508">
          {"14040a01-1226-4438-bb70-e23cbbe298a5":{"roots":{"references":[{"attributes":{"callback":null,"factors":["2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017"],"range_padding":0.1},"id":"7f16b5bc-0517-4c2a-a660-72597984a910","type":"FactorRange"},{"attributes":{"bottom":{"expr":{"id":"7c88e42a-22c0-4067-ac67-08e4b5caba8f","type":"Stack"}},"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"top":{"expr":{"id":"efc01efc-0b92-46dd-b580-ff5e685a5816","type":"Stack"}},"width":{"value":0.5},"x":{"field":"Year"}},"id":"63723f5e-6c30-4f8c-ba85-cef639922408","type":"VBar"},{"attributes":{},"id":"adc754cb-2de2-415a-8687-4a52b2f9a759","type":"BasicTickFormatter"},{"attributes":{"below":[{"id":"5cbb1128-51d4-412f-be86-7a60fbf9613a","type":"CategoricalAxis"}],"left":[{"id":"c62b8529-83d5-4ca4-b366-ab4accdd0c33","type":"LinearAxis"}],"outline_line_color":{"value":null},"plot_height":350,"renderers":[{"id":"5cbb1128-51d4-412f-be86-7a60fbf9613a","type":"CategoricalAxis"},{"id":"1f24e999-6dcf-4b93-9c4d-f0fb457a0ed3","type":"Grid"},{"id":"c62b8529-83d5-4ca4-b366-ab4accdd0c33","type":"LinearAxis"},{"id":"2b59dbfd-cb26-422f-8e30-6a62ddbf1bf6","type":"Grid"},{"id":"731924cf-0e2d-493b-8bf5-861045d22731","type":"GlyphRenderer"},{"id":"f406f534-4859-4445-a1f3-e7c514bd5de6","type":"GlyphRenderer"}],"title":{"id":"c719d756-94c2-4d50-bd84-a6711dfe7413","type":"Title"},"toolbar":{"id":"4eec4505-1882-41f7-b5ff-cea5cb07aec8","type":"Toolbar"},"toolbar_location":null,"x_range":{"id":"7f16b5bc-0517-4c2a-a660-72597984a910","type":"FactorRange"},"x_scale":{"id":"9c96dbe9-fe67-40e9-a039-bfc8159ee0f7","type":"CategoricalScale"},"y_range":{"id":"b20aa497-ea92-448a-8813-077abe752a91","type":"DataRange1d"},"y_scale":{"id":"6a037768-319c-453c-9367-6360e303cb9e","type":"LinearScale"}},"id":"ebe796a5-2dac-49e8-b400-24ad00df1d1f","subtype":"Figure","type":"Plot"},{"attributes":{"data_source":{"id":"5884fa69-0dd9-4e3e-aa38-58014d27799a","type":"ColumnDataSource"},"glyph":{"id":"0f403c3a-1e0e-40bf-90ba-dc8de0b21dd2","type":"VBar"},"hover_glyph":null,"muted_glyph":null,"name":"True","nonselection_glyph":{"id":"ec0144ea-cbed-4eac-aaa6-48be3e648012","type":"VBar"},"selection_glyph":null,"view":{"id":"fd3c6ccf-6e83-41a5-b0a6-aaf1a05198e2","type":"CDSView"}},"id":"731924cf-0e2d-493b-8bf5-861045d22731","type":"GlyphRenderer"},{"attributes":{"callback":null,"renderers":[{"id":"731924cf-0e2d-493b-8bf5-861045d22731","type":"GlyphRenderer"}],"tooltips":[["True total","@True"],["index","$index"]]},"id":"8b0556b6-bb8f-41a1-8283-0aa8bce76046","type":"HoverTool"},{"attributes":{"bottom":{"expr":{"id":"7c88e42a-22c0-4067-ac67-08e4b5caba8f","type":"Stack"}},"fill_color":{"value":"#f49f9f"},"line_color":{"value":"#f49f9f"},"top":{"expr":{"id":"efc01efc-0b92-46dd-b580-ff5e685a5816","type":"Stack"}},"width":{"value":0.5},"x":{"field":"Year"}},"id":"43f7a0ca-29cc-4d3f-ad79-07fd74414522","type":"VBar"},{"attributes":{"children":[{"id":"c00258a7-f7bb-4784-9845-2ceddc385654","type":"Dropdown"},{"id":"1c0baf44-5af6-4b3f-a616-61570e3e63fe","type":"RangeSlider"},{"id":"939f09b5-5721-4aa8-ade1-0cd2cb865d84","type":"Toggle"}]},"id":"c3879442-f5ce-4eb7-83dc-a56e65edf7bd","type":"WidgetBox"},{"attributes":{"callback":null,"end":2018,"start":2001,"title":"Year","value":[2002,2017]},"id":"1c0baf44-5af6-4b3f-a616-61570e3e63fe","type":"RangeSlider"},{"attributes":{"data_source":{"id":"5884fa69-0dd9-4e3e-aa38-58014d27799a","type":"ColumnDataSource"},"glyph":{"id":"43f7a0ca-29cc-4d3f-ad79-07fd74414522","type":"VBar"},"hover_glyph":null,"muted_glyph":null,"name":"False","nonselection_glyph":{"id":"63723f5e-6c30-4f8c-ba85-cef639922408","type":"VBar"},"selection_glyph":null,"view":{"id":"03480479-a8f3-4718-b04f-dffd567ffa71","type":"CDSView"}},"id":"f406f534-4859-4445-a1f3-e7c514bd5de6","type":"GlyphRenderer"},{"attributes":{"button_type":"success","callback":null,"icon":null,"label":"By Type"},"id":"939f09b5-5721-4aa8-ade1-0cd2cb865d84","type":"Toggle"},{"attributes":{"source":{"id":"5884fa69-0dd9-4e3e-aa38-58014d27799a","type":"ColumnDataSource"}},"id":"fd3c6ccf-6e83-41a5-b0a6-aaf1a05198e2","type":"CDSView"},{"attributes":{"source":{"id":"5884fa69-0dd9-4e3e-aa38-58014d27799a","type":"ColumnDataSource"}},"id":"03480479-a8f3-4718-b04f-dffd567ffa71","type":"CDSView"},{"attributes":{"callback":null,"start":0},"id":"b20aa497-ea92-448a-8813-077abe752a91","type":"DataRange1d"},{"attributes":{"button_type":"warning","callback":null,"icon":null,"label":"Select Business","menu":[["A' Cappella Bistro, 1301 S Michigan","A' Cappella Bistro"],["A Mano, 335 N Dearborn St","A Mano"],["Abou Andre, 60 E Jackson Blvd","Abou Andre"],["Ada's Famous Deli, 14 S Wabash Ave","Ada's Famous Deli"],["Alain's, 1355 S Michigan Ave","Alain's"],["Allstars Sports Bar &amp; Grill, 205 W Wacker Dr","Allstars Sports Bar &amp; Grill"],["Alonti Cafe, 401 S Lasalle St","Alonti Cafe"],["Alonti Cafe, 225 N Michigan Ave","Alonti Cafe"],["Alonti Cafe, 177 W Washington St","Alonti Cafe"],["Alonti Deli, 2 N Riverside Plz","Alonti Deli"],["Alonti Deli, 300 S Riverside Plz","Alonti Deli"],["Alonti Market Cafe, 1 N Franklin St","Alonti Market Cafe"],["Al's Beef, 28 E Jackson Dr","Al's Beef"],["Amarit Thai Restaurant, 600 S Dearborn St","Amarit Thai Restaurant"],["Americana Submarine, 400 S Clark St","Americana Submarine"],["America's Dog, 21 E Adams St","America's Dog"],["America's Dog, 26 E Randolph St","America's Dog"],["Ara On, 160 W Adams St","Ara On"],["Arby's, 195 N Dearborn St","Arby's"],["Arby's, 20 E Jackson Blvd","Arby's"],["Arby's, 100 W Randolph St","Arby's"],["Aria, 200 N Columbus Dr","Aria"],["Armand's Pizzeria, 151 E Randall Rd","Armand's Pizzeria"],["Around the Corner, 325 S Franklin St","Around the Corner"],["Artist's Cafe, 412 S Michigan Ave","Artist's Cafe"],["Artist's Cafe, 1150 S Wabash","Artist's Cafe"],["Arturo Express, 122 S Canal St","Arturo Express"],["Asian Chao and Villa Italian, 18 W Jackson Blvd","Asian Chao and Villa Italian"],["Atwood Cafe, 1 W Washington St","Atwood Cafe"],["Au Bon Pain, 125 S Wacker Dr","Au Bon Pain"],["Au Bon Pain, 181 W Madison St","Au Bon Pain"],["Au Bon Pain, 210 S Canal St","Au Bon Pain"],["Au Bon Pain, 108 N State","Au Bon Pain"],["Au Bon Pain, 200 E Randolph St","Au Bon Pain"],["Au Bon Pain, 200 W Adams St","Au Bon Pain"],["Augustino's Rock &amp; Roll Deli, 233 S Wacker Dr","Augustino's Rock &amp; Roll Deli"],["Argo Tea, 16 W Randolph St","Argo Tea"],["Argo Tea, 140 S Dearborn St","Argo Tea"],["Australian Homemade, 111 N State St","Australian Homemade"],["Angels &amp; Kings, 230 N Michigan Ave","Angels &amp; Kings"],["Avanti Caff\u00c3\u0192\u00c2\u00a9, 200 W Jackson Blvd","Avanti Caff\u00c3\u0192\u00c2\u00a9"],["Avec, 615 W Randolph St","Avec"]]},"id":"c00258a7-f7bb-4784-9845-2ceddc385654","type":"Dropdown"},{"attributes":{"callback":null,"renderers":[{"id":"f406f534-4859-4445-a1f3-e7c514bd5de6","type":"GlyphRenderer"}],"tooltips":[["False total","@False"],["index","$index"]]},"id":"1706b880-dfef-44a6-bb27-ac0257e1c591","type":"HoverTool"},{"attributes":{"children":[{"id":"c3879442-f5ce-4eb7-83dc-a56e65edf7bd","type":"WidgetBox"},{"id":"ebe796a5-2dac-49e8-b400-24ad00df1d1f","subtype":"Figure","type":"Plot"}],"width":800},"id":"60954e4a-6693-4941-9052-471f3882557a","type":"Row"},{"attributes":{"plot":null,"text":"Arrests per Year per Business"},"id":"c719d756-94c2-4d50-bd84-a6711dfe7413","type":"Title"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_scroll":"auto","active_tap":"auto","tools":[{"id":"8b0556b6-bb8f-41a1-8283-0aa8bce76046","type":"HoverTool"},{"id":"1706b880-dfef-44a6-bb27-ac0257e1c591","type":"HoverTool"}]},"id":"4eec4505-1882-41f7-b5ff-cea5cb07aec8","type":"Toolbar"},{"attributes":{},"id":"9c96dbe9-fe67-40e9-a039-bfc8159ee0f7","type":"CategoricalScale"},{"attributes":{},"id":"6a037768-319c-453c-9367-6360e303cb9e","type":"LinearScale"},{"attributes":{"formatter":{"id":"adc754cb-2de2-415a-8687-4a52b2f9a759","type":"BasicTickFormatter"},"minor_tick_line_color":{"value":null},"plot":{"id":"ebe796a5-2dac-49e8-b400-24ad00df1d1f","subtype":"Figure","type":"Plot"},"ticker":{"id":"e687c248-f0a8-4095-a897-f0e4f9ee0595","type":"BasicTicker"}},"id":"c62b8529-83d5-4ca4-b366-ab4accdd0c33","type":"LinearAxis"},{"attributes":{"formatter":{"id":"f0516c53-2ef3-47d7-abd9-df415bbf3a47","type":"CategoricalTickFormatter"},"major_label_orientation":1.2,"minor_tick_line_color":{"value":null},"plot":{"id":"ebe796a5-2dac-49e8-b400-24ad00df1d1f","subtype":"Figure","type":"Plot"},"ticker":{"id":"95ec58fc-420f-45a7-b5c0-4dc52c9b15f2","type":"CategoricalTicker"}},"id":"5cbb1128-51d4-412f-be86-7a60fbf9613a","type":"CategoricalAxis"},{"attributes":{"bottom":{"expr":{"id":"2374245c-92ee-417b-b2f3-b4a43c0fc719","type":"Stack"}},"fill_color":{"value":"#d1edb1"},"line_color":{"value":"#d1edb1"},"top":{"expr":{"id":"a889468f-277f-4c0e-bf58-630929d409b0","type":"Stack"}},"width":{"value":0.5},"x":{"field":"Year"}},"id":"0f403c3a-1e0e-40bf-90ba-dc8de0b21dd2","type":"VBar"},{"attributes":{},"id":"95ec58fc-420f-45a7-b5c0-4dc52c9b15f2","type":"CategoricalTicker"},{"attributes":{"grid_line_color":{"value":null},"plot":{"id":"ebe796a5-2dac-49e8-b400-24ad00df1d1f","subtype":"Figure","type":"Plot"},"ticker":{"id":"95ec58fc-420f-45a7-b5c0-4dc52c9b15f2","type":"CategoricalTicker"}},"id":"1f24e999-6dcf-4b93-9c4d-f0fb457a0ed3","type":"Grid"},{"attributes":{},"id":"f0516c53-2ef3-47d7-abd9-df415bbf3a47","type":"CategoricalTickFormatter"},{"attributes":{},"id":"e687c248-f0a8-4095-a897-f0e4f9ee0595","type":"BasicTicker"},{"attributes":{"dimension":1,"plot":{"id":"ebe796a5-2dac-49e8-b400-24ad00df1d1f","subtype":"Figure","type":"Plot"},"ticker":{"id":"e687c248-f0a8-4095-a897-f0e4f9ee0595","type":"BasicTicker"}},"id":"2b59dbfd-cb26-422f-8e30-6a62ddbf1bf6","type":"Grid"},{"attributes":{"fields":["True","False"]},"id":"efc01efc-0b92-46dd-b580-ff5e685a5816","type":"Stack"},{"attributes":{"callback":null,"column_names":["Year","True","False"],"data":{"False":[91,80,93,101,93,88,95,73,56,84,67,52,61,68,72,89],"True":[31,30,36,32,35,21,16,17,20,17,9,26,23,19,9,14],"Year":["2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017"]},"selected":null,"selection_policy":null},"id":"5884fa69-0dd9-4e3e-aa38-58014d27799a","type":"ColumnDataSource"},{"attributes":{"fields":["True"]},"id":"a889468f-277f-4c0e-bf58-630929d409b0","type":"Stack"},{"attributes":{"fields":[]},"id":"2374245c-92ee-417b-b2f3-b4a43c0fc719","type":"Stack"},{"attributes":{"fields":["True"]},"id":"7c88e42a-22c0-4067-ac67-08e4b5caba8f","type":"Stack"},{"attributes":{"bottom":{"expr":{"id":"2374245c-92ee-417b-b2f3-b4a43c0fc719","type":"Stack"}},"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"top":{"expr":{"id":"a889468f-277f-4c0e-bf58-630929d409b0","type":"Stack"}},"width":{"value":0.5},"x":{"field":"Year"}},"id":"ec0144ea-cbed-4eac-aaa6-48be3e648012","type":"VBar"}],"root_ids":["60954e4a-6693-4941-9052-471f3882557a"]},"title":"Bokeh Application","version":"0.12.15"}}
        </script>
        <script type="text/javascript">
          (function() {
            var fn = function() {
              Bokeh.safely(function() {
                (function(root) {
                  function embed_document(root) {
                    
                  var docs_json = document.getElementById('9df50690-6594-4642-b3dc-d87cfa269508').textContent;
                  var render_items = [{"docid":"14040a01-1226-4438-bb70-e23cbbe298a5","elementid":"7f439432-1a50-4d70-8442-a025a3c7c387","modelid":"60954e4a-6693-4941-9052-471f3882557a"}];
                  root.Bokeh.embed.embed_items(docs_json, render_items);
                
                  }
                  if (root.Bokeh !== undefined) {
                    embed_document(root);
                  } else {
                    var attempts = 0;
                    var timer = setInterval(function(root) {
                      if (root.Bokeh !== undefined) {
                        embed_document(root);
                        clearInterval(timer);
                      }
                      attempts++;
                      if (attempts > 100) {
                        console.log("Bokeh: ERROR: Unable to run BokehJS code because BokehJS library is missing")
                        clearInterval(timer);
                      }
                    }, 10, root)
                  }
                })(window);
              });
            };
            if (document.readyState != "loading") fn();
            else document.addEventListener("DOMContentLoaded", fn);
          })();
        </script>
    </body>
</html>

{:/}
