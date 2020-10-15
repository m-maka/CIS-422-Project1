'''
Authors: Brandon Bower along with Max Aguirre and Mapuana Maka

'''

import googlemaps

def getDirections(client, segments):
    #result = client.directions(latlongs[0], latlongs[1])
    #print(result)

    return  None


def createSegments(latlongs):
    length = len(latlongs)
    segNumb = (length // 12) + 1
    index = 0
    segments = []
    for segment in range(segNumb):
        #print(f'start (index {index})')
        segments.append({'start' : latlongs[index]})
        #wp = 1
        waypoints = []
        index += 1
        for index in range(index, min(index + 10,length - 2)):
            #print(f'wp, {wp} (index {index})')
            #wp += 1
            waypoints.append(f'via:{latlongs[index]}')
        if len(waypoints):
            segments[segment]['waypoints'] = waypoints
            index += 1
        #print(f'end (index {index})')
        segments[segment]['end'] = latlongs[index]
    return segments
    
    
    



def main():
    latlongs = [(44.2185374, -123.2125012), (44.21857, -123.21163),
                (44.21898, -123.21158), (44.2190527, -123.2089076),
                (44.2225, -123.20905), (44.2223507, -123.2147348),
                (44.22415, -123.21471), (44.22468, -123.21394),
                (44.2264858, -123.2139206)]
    '''
    latlongs = [(44.587662, -123.256691), (44.587395, -123.262154), (44.587502, -123.262497),
                (44.596886, -123.262482), (44.598633, -123.26149), (44.599155, -123.261673),
                (44.60146, -123.263374), (44.602081, -123.263222),(44.602959, -123.262421),
                (44.603649, -123.262161), (44.612709, -123.262253), (44.613117, -123.267418),
                (44.613689, -123.268028), (44.616093, -123.268036), (44.616718, -123.268425),
                (44.616905, -123.26915), (44.616951, -123.274727), (44.6172449, -123.275269),
                (44.618179, -123.275856), (44.618835, -123.275887), (44.6216579, -123.275101),
                (44.622791, -123.274361),(44.62421, -123.27401), (44.626221, -123.27269)]
    '''
    #gmaps = googlemaps.Client(key='You Key Here')
    segments = createSegments(latlongs)
    #turnDetect(gmaps, segments)


if __name__ == '__main__':
    main()
