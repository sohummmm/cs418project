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
            <div class="bk-plotdiv" id="cc44e23c-434c-4c89-b8ab-52df11246ec6"></div>
        </div>
        
        <script type="application/json" id="3cd0e1d8-73ef-4970-892d-9350557d5839">
          {"4ea7444e-f793-4759-bea7-86f5d6bc1775":{"roots":{"references":[{"attributes":{},"id":"0f2db817-d7fe-49f5-8eaa-df24426b6f68","type":"CategoricalTickFormatter"},{"attributes":{"callback":null,"end":2018,"start":2001,"title":"Year","value":[2002,2017]},"id":"ed7bfd72-8dd4-4bc9-81db-2b7c441e6e92","type":"RangeSlider"},{"attributes":{"children":[{"id":"5fdc6bfb-0a2b-49f6-a20d-d0fe9ad748f2","type":"WidgetBox"},{"id":"1b3f89a7-b790-4c71-b27f-d321d0e69953","subtype":"Figure","type":"Plot"}],"width":800},"id":"e7dd37d4-d760-4aab-8642-ffe057c2597a","type":"Row"},{"attributes":{"source":{"id":"9a4977bc-af78-4144-8520-80de353484ac","type":"ColumnDataSource"}},"id":"4a67b71d-a72b-4c27-b415-0c5c89f80d12","type":"CDSView"},{"attributes":{"plot":null,"text":"Arrests per Crime Type per Business"},"id":"9b8f480b-cd59-4eca-a5b7-d6a057d2f752","type":"Title"},{"attributes":{"data_source":{"id":"9a4977bc-af78-4144-8520-80de353484ac","type":"ColumnDataSource"},"glyph":{"id":"f33cce73-a8c2-40fd-ac74-e3b842b655f0","type":"VBar"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"dcd773d8-5fdc-414f-aeb9-8ce7068194f0","type":"VBar"},"selection_glyph":null,"view":{"id":"1398ecbf-c3e2-47df-af25-168f6500e40b","type":"CDSView"}},"id":"d3493692-53ab-4e8f-ad53-5c6a432dbc71","type":"GlyphRenderer"},{"attributes":{"callback":null,"start":0},"id":"4c7fe69d-8f2d-4e4b-aef7-42a6f2f8a7c2","type":"DataRange1d"},{"attributes":{"source":{"id":"9a4977bc-af78-4144-8520-80de353484ac","type":"ColumnDataSource"}},"id":"1398ecbf-c3e2-47df-af25-168f6500e40b","type":"CDSView"},{"attributes":{"button_type":"warning","callback":null,"icon":null,"label":"Select Business","menu":[["A' Cappella Bistro, 1301 S Michigan","A' Cappella Bistro"],["A Mano, 335 N Dearborn St","A Mano"],["Abou Andre, 60 E Jackson Blvd","Abou Andre"],["Ada's Famous Deli, 14 S Wabash Ave","Ada's Famous Deli"],["Alain's, 1355 S Michigan Ave","Alain's"],["Allstars Sports Bar &amp; Grill, 205 W Wacker Dr","Allstars Sports Bar &amp; Grill"],["Alonti Cafe, 401 S Lasalle St","Alonti Cafe"],["Alonti Cafe, 225 N Michigan Ave","Alonti Cafe"],["Alonti Cafe, 177 W Washington St","Alonti Cafe"],["Alonti Deli, 2 N Riverside Plz","Alonti Deli"],["Alonti Deli, 300 S Riverside Plz","Alonti Deli"],["Alonti Market Cafe, 1 N Franklin St","Alonti Market Cafe"],["Al's Beef, 28 E Jackson Dr","Al's Beef"],["Amarit Thai Restaurant, 600 S Dearborn St","Amarit Thai Restaurant"],["Americana Submarine, 400 S Clark St","Americana Submarine"],["America's Dog, 21 E Adams St","America's Dog"],["America's Dog, 26 E Randolph St","America's Dog"],["Ara On, 160 W Adams St","Ara On"],["Arby's, 195 N Dearborn St","Arby's"],["Arby's, 20 E Jackson Blvd","Arby's"],["Arby's, 100 W Randolph St","Arby's"],["Aria, 200 N Columbus Dr","Aria"],["Armand's Pizzeria, 151 E Randall Rd","Armand's Pizzeria"],["Around the Corner, 325 S Franklin St","Around the Corner"],["Artist's Cafe, 412 S Michigan Ave","Artist's Cafe"],["Artist's Cafe, 1150 S Wabash","Artist's Cafe"],["Arturo Express, 122 S Canal St","Arturo Express"],["Asian Chao and Villa Italian, 18 W Jackson Blvd","Asian Chao and Villa Italian"],["Atwood Cafe, 1 W Washington St","Atwood Cafe"],["Au Bon Pain, 125 S Wacker Dr","Au Bon Pain"],["Au Bon Pain, 181 W Madison St","Au Bon Pain"],["Au Bon Pain, 210 S Canal St","Au Bon Pain"],["Au Bon Pain, 108 N State","Au Bon Pain"],["Au Bon Pain, 200 E Randolph St","Au Bon Pain"],["Au Bon Pain, 200 W Adams St","Au Bon Pain"],["Augustino's Rock &amp; Roll Deli, 233 S Wacker Dr","Augustino's Rock &amp; Roll Deli"],["Argo Tea, 16 W Randolph St","Argo Tea"],["Argo Tea, 140 S Dearborn St","Argo Tea"],["Australian Homemade, 111 N State St","Australian Homemade"],["Angels &amp; Kings, 230 N Michigan Ave","Angels &amp; Kings"],["Avanti Caff\u00c3\u0192\u00c2\u00a9, 200 W Jackson Blvd","Avanti Caff\u00c3\u0192\u00c2\u00a9"],["Avec, 615 W Randolph St","Avec"]]},"id":"4d980607-124a-49a5-9d1a-c2ac90b57322","type":"Dropdown"},{"attributes":{"callback":null,"factors":["2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017"],"range_padding":0.1},"id":"190cff04-1fa8-4042-b4b8-3d5988062617","type":"FactorRange"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_scroll":"auto","active_tap":"auto"},"id":"05e289e1-98f2-4c33-a7ba-d037075ce495","type":"Toolbar"},{"attributes":{},"id":"6befb2e3-f956-49db-8ddd-70ca84e17362","type":"CategoricalScale"},{"attributes":{},"id":"85ccbd0e-7116-4604-b5a0-ada5158386f8","type":"LinearScale"},{"attributes":{"formatter":{"id":"be6868e5-8b74-4fac-bdb1-11e90b287a39","type":"BasicTickFormatter"},"minor_tick_line_color":{"value":null},"plot":{"id":"1b3f89a7-b790-4c71-b27f-d321d0e69953","subtype":"Figure","type":"Plot"},"ticker":{"id":"a3f3cead-c03b-4d24-8006-0f340563e7a6","type":"BasicTicker"}},"id":"963ebb98-6715-4258-b6b0-cf8d33360028","type":"LinearAxis"},{"attributes":{"formatter":{"id":"0f2db817-d7fe-49f5-8eaa-df24426b6f68","type":"CategoricalTickFormatter"},"major_label_orientation":1.2,"minor_tick_line_color":{"value":null},"plot":{"id":"1b3f89a7-b790-4c71-b27f-d321d0e69953","subtype":"Figure","type":"Plot"},"ticker":{"id":"ed14a418-f44c-4827-8be8-a82a8b6864d0","type":"CategoricalTicker"}},"id":"e5dfe8a1-5793-42f4-8e3b-2885454fbcff","type":"CategoricalAxis"},{"attributes":{},"id":"be6868e5-8b74-4fac-bdb1-11e90b287a39","type":"BasicTickFormatter"},{"attributes":{},"id":"ed14a418-f44c-4827-8be8-a82a8b6864d0","type":"CategoricalTicker"},{"attributes":{"grid_line_color":{"value":null},"plot":{"id":"1b3f89a7-b790-4c71-b27f-d321d0e69953","subtype":"Figure","type":"Plot"},"ticker":{"id":"ed14a418-f44c-4827-8be8-a82a8b6864d0","type":"CategoricalTicker"}},"id":"93a9d88f-fd21-45da-9c82-2ff65434a747","type":"Grid"},{"attributes":{"callback":null,"column_names":["Year","True","False"],"data":{"False":[91,80,93,101,93,88,95,73,56,84,67,52,61,68,72,89],"True":[31,30,36,32,35,21,16,17,20,17,9,26,23,19,9,14],"Year":["2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017"]},"selected":null,"selection_policy":null},"id":"9a4977bc-af78-4144-8520-80de353484ac","type":"ColumnDataSource"},{"attributes":{},"id":"a3f3cead-c03b-4d24-8006-0f340563e7a6","type":"BasicTicker"},{"attributes":{"dimension":1,"plot":{"id":"1b3f89a7-b790-4c71-b27f-d321d0e69953","subtype":"Figure","type":"Plot"},"ticker":{"id":"a3f3cead-c03b-4d24-8006-0f340563e7a6","type":"BasicTicker"}},"id":"86143f8b-4dca-47a4-9847-4b9a9b89f930","type":"Grid"},{"attributes":{"fields":["True","False"]},"id":"0070de8e-d69f-4a88-8b62-b88cff000def","type":"Stack"},{"attributes":{"bottom":{"expr":{"id":"ddb8e524-7f3d-47ad-817b-96d9a8bcc1a2","type":"Stack"}},"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"top":{"expr":{"id":"e3c77296-ef45-4b06-a3fa-bd9a82d6de9b","type":"Stack"}},"width":{"value":0.5},"x":{"field":"Year"}},"id":"6a25aeda-2542-494f-a5b7-60ad5557e414","type":"VBar"},{"attributes":{"bottom":{"expr":{"id":"ddb8e524-7f3d-47ad-817b-96d9a8bcc1a2","type":"Stack"}},"fill_color":{"value":"#d1edb1"},"line_color":{"value":"#d1edb1"},"top":{"expr":{"id":"e3c77296-ef45-4b06-a3fa-bd9a82d6de9b","type":"Stack"}},"width":{"value":0.5},"x":{"field":"Year"}},"id":"7d9c285c-09ca-49df-9b87-148b421a18e9","type":"VBar"},{"attributes":{"fields":["True"]},"id":"e3c77296-ef45-4b06-a3fa-bd9a82d6de9b","type":"Stack"},{"attributes":{"fields":[]},"id":"ddb8e524-7f3d-47ad-817b-96d9a8bcc1a2","type":"Stack"},{"attributes":{"button_type":"success","callback":null,"icon":null,"label":"By Type"},"id":"74127d49-8dfa-4e0f-8699-a6563bcbca33","type":"Toggle"},{"attributes":{"fields":["True"]},"id":"76e41edb-b042-47b1-a9e1-f6cf53ff205c","type":"Stack"},{"attributes":{"children":[{"id":"4d980607-124a-49a5-9d1a-c2ac90b57322","type":"Dropdown"},{"id":"ed7bfd72-8dd4-4bc9-81db-2b7c441e6e92","type":"RangeSlider"},{"id":"74127d49-8dfa-4e0f-8699-a6563bcbca33","type":"Toggle"}]},"id":"5fdc6bfb-0a2b-49f6-a20d-d0fe9ad748f2","type":"WidgetBox"},{"attributes":{"below":[{"id":"e5dfe8a1-5793-42f4-8e3b-2885454fbcff","type":"CategoricalAxis"}],"left":[{"id":"963ebb98-6715-4258-b6b0-cf8d33360028","type":"LinearAxis"}],"outline_line_color":{"value":null},"plot_height":350,"renderers":[{"id":"e5dfe8a1-5793-42f4-8e3b-2885454fbcff","type":"CategoricalAxis"},{"id":"93a9d88f-fd21-45da-9c82-2ff65434a747","type":"Grid"},{"id":"963ebb98-6715-4258-b6b0-cf8d33360028","type":"LinearAxis"},{"id":"86143f8b-4dca-47a4-9847-4b9a9b89f930","type":"Grid"},{"id":"db9fb6a3-00bc-4609-88bc-a621d6c81370","type":"GlyphRenderer"},{"id":"d3493692-53ab-4e8f-ad53-5c6a432dbc71","type":"GlyphRenderer"}],"title":{"id":"9b8f480b-cd59-4eca-a5b7-d6a057d2f752","type":"Title"},"toolbar":{"id":"05e289e1-98f2-4c33-a7ba-d037075ce495","type":"Toolbar"},"toolbar_location":null,"x_range":{"id":"190cff04-1fa8-4042-b4b8-3d5988062617","type":"FactorRange"},"x_scale":{"id":"6befb2e3-f956-49db-8ddd-70ca84e17362","type":"CategoricalScale"},"y_range":{"id":"4c7fe69d-8f2d-4e4b-aef7-42a6f2f8a7c2","type":"DataRange1d"},"y_scale":{"id":"85ccbd0e-7116-4604-b5a0-ada5158386f8","type":"LinearScale"}},"id":"1b3f89a7-b790-4c71-b27f-d321d0e69953","subtype":"Figure","type":"Plot"},{"attributes":{"data_source":{"id":"9a4977bc-af78-4144-8520-80de353484ac","type":"ColumnDataSource"},"glyph":{"id":"7d9c285c-09ca-49df-9b87-148b421a18e9","type":"VBar"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"6a25aeda-2542-494f-a5b7-60ad5557e414","type":"VBar"},"selection_glyph":null,"view":{"id":"4a67b71d-a72b-4c27-b415-0c5c89f80d12","type":"CDSView"}},"id":"db9fb6a3-00bc-4609-88bc-a621d6c81370","type":"GlyphRenderer"},{"attributes":{"bottom":{"expr":{"id":"76e41edb-b042-47b1-a9e1-f6cf53ff205c","type":"Stack"}},"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"top":{"expr":{"id":"0070de8e-d69f-4a88-8b62-b88cff000def","type":"Stack"}},"width":{"value":0.5},"x":{"field":"Year"}},"id":"dcd773d8-5fdc-414f-aeb9-8ce7068194f0","type":"VBar"},{"attributes":{"bottom":{"expr":{"id":"76e41edb-b042-47b1-a9e1-f6cf53ff205c","type":"Stack"}},"fill_color":{"value":"#f49f9f"},"line_color":{"value":"#f49f9f"},"top":{"expr":{"id":"0070de8e-d69f-4a88-8b62-b88cff000def","type":"Stack"}},"width":{"value":0.5},"x":{"field":"Year"}},"id":"f33cce73-a8c2-40fd-ac74-e3b842b655f0","type":"VBar"}],"root_ids":["e7dd37d4-d760-4aab-8642-ffe057c2597a"]},"title":"Bokeh Application","version":"0.12.15"}}
        </script>
        <script type="text/javascript">
          (function() {
            var fn = function() {
              Bokeh.safely(function() {
                (function(root) {
                  function embed_document(root) {
                    
                  var docs_json = document.getElementById('3cd0e1d8-73ef-4970-892d-9350557d5839').textContent;
                  var render_items = [{"docid":"4ea7444e-f793-4759-bea7-86f5d6bc1775","elementid":"cc44e23c-434c-4c89-b8ab-52df11246ec6","modelid":"e7dd37d4-d760-4aab-8642-ffe057c2597a"}];
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
