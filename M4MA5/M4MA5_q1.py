import pygal #needed for visualization

places = ['Hyuganada Sea, Japan', 'NW of Grapevine, CA', \
          'SW of Lamont, CA', 'E of Barcelona,Phillipines']
mags = [7.1, 4.44, 5.22, 6.3]

quakehist = pygal.Bar() #create visualization

quakehist.add('', mags) #add values for quake magnitudes

#label axes and add title
quakehist.title = "Significant Earthquakes in the Past 7 Days"
quakehist.x_labels = places
quakehist.x_title = "Location"
quakehist.y_title = "Magnitude(Richter Scale)"

quakehist.render_to_file('nm_quakes_week.svg') #create file in current directory

