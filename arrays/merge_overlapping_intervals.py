"""
- problem: merge overlapping intervals in a list...think of a number line with overlapping intervals
- solution: have a new output mergedIntervals array, and append to it the nextInterval
the next interval will be updated by the currentInterval which itself is updated if there is an overlap.
The loop will go up every time it has to update the currentInterval, or if it doesn't need to update the currInterval
then the currInterval will equal the nextInterval and only then repeat the loop again.
- complexity: O(nlogn) time upperbounded by sorting algorithm, and O(n) space for the intervals
"""
def mergeOverlappingIntervals(intervals):
	# sort interval subarrays by the first/0'th element 
    sortedIntervals = sorted(intervals, key = lambda x: x[0])
	
	mergedIntervals = []
	# need to have at least one value: (this assumes the input is non-empty...check with interviewer)
	currentInterval = sortedIntervals[0]
	mergedIntervals.append(currentInterval)

	# go through each interval and update the curr interval to merge if there is something to merge, otherwise just add it
	for nextInterval in sortedIntervals:
		_, currentIntervalEnd = currentInterval # same as currentIntervalEnd = currentInterval[1]
		nextIntervalStart, nextIntervalEnd = nextInterval  # same as nextIntervalStart, .. = s...[0], s..[1]
	
		# update the current interval as needed and the loop will be restarted again
		if currentIntervalEnd >= nextIntervalStart:
			currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
		
		# if we don't need to update the current interval again, then set the current inter. to be the next interval just add it to the merged intervals
		else:
			currentInterval = nextInterval
			mergedIntervals.append(currentInterval)
		
	return mergedIntervals


#--------------------------------my failed attempt
# assume input is non-empty and there are no edge cases (non numerical input or wrong size) and no wrong order
# return output as a new array (of arrays)
def mergeOverlappingIntervals(intervals):
    if len(intervals) <= 1: # in case of an edge case 
		return intervals
	mergedIntervals = []
	for ind, interval in enumerate(intervals[1:]): # start from the 1'th subarray/interval
		if interval[]
    return mergedIntervals 

