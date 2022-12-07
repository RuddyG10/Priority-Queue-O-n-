import random
import time

from PQ import PriorityQueue


def test_insertion_extraction(num_elements, num_trials):
    # Show test header
    print()
    print('------------------------------------')
    print('  TESTING INSERTION AND EXTRACTION  ')
    print('------------------------------------')
    print()

    # Run test num trials
    for trial in range(num_trials):
        # Generate random numbers
        a = [i for i in range(num_elements)]
        random.shuffle(a)

        # Create priority queue
        pq = PriorityQueue()

        # Insert elements in PQ
        for x in a:
            # Insert element and priority
            pq.insert_or_update(x, str(x))

        # Set failed flag
        failed_trial = False

        # Testing extraction (in order)
        for i in range(num_elements):
            # Get item
            item = pq.extract()
            priority = item[0]
            data = item[1]

            # Check item
            if priority != i:
                # Set failed flag
                failed_trial = True

                # Print error
                print('   FAIL: Element #%d is %d' % (i, priority))

                # Break trial
                break

        # Check empty PQ should return None
        item = pq.extract()
        if item != None:
                # Set failed flag
                failed_trial = True

                # Print error
                print('   FAIL: Empty PQ should have returned NONE')
                
        # Print test result
        if failed_trial:
            # Print failed trial
            print('Trial #%2d: FAIL' % (trial + 1))
        else:
            # Print success trial
            print('Trial #%2d: OK' % (trial + 1))



def test_insertion_update_extraction(num_elements, num_trials):
    # Show test header
    print()
    print('--------------------------------------------')
    print('  TESTING INSERTION, UPDATE AND EXTRACTION  ')
    print('--------------------------------------------')
    print()

    # Run test num trials
    for trial in range(num_trials):
        # Empty insertion list
        a = []
        
        # Generate random numbers and three types of priorities
        for i in range(num_elements):
            a.append((i + 0 * num_elements, str(i)))
            a.append((i + 1 * num_elements, str(i)))
            a.append((i + 2 * num_elements, str(i)))

        random.shuffle(a)

        # Create priority queue
        pq = PriorityQueue()

        # Insert elements in PQ
        for x in a:
            # Get item and priority
            priority, data = x
            
            # Insert element and priority
            pq.insert_or_update(priority, data)

        #print pq

        # Generate random numbers
        #a = [i for i in range(num_elements)]
        #random.shuffle(a)

        # Update elements
        #for x in a:
            # Insert element and priority
            #pq.insert_or_update(x, str(x))

        #print pq


        # Set failed flag
        failed_trial = False

        # Testing extraction (in order)
        for i in range(num_elements):
            # Get item
            item = pq.extract()
            priority = item[0]
            data = item[1]

            # Check item
            if priority != i:
                # Set failed flag
                failed_trial = True

                # Print error
                print('   FAIL: Element #%d is %d' % (i, priority))

                # Break trial
                break

        # Print test result
        if failed_trial:
            # Print failed trial
            print ('Trial #%2d: FAIL' % (trial + 1))
        else:
             # Print success trial
            print ('Trial #%2d: OK' % (trial + 1))






def test_timed_insertion_extraction(elements, num_trials):
    # Show test header
    print()
    print('------------------------------------------')
    print('  TESTING TIMED INSERTION AND EXTRACTION  ')
    print('------------------------------------------')
    print()

    for num_elements in elements:
        # Init total elapsed time
        total_time = 0.0

        # Print header
        print('Number of elements = %d' % num_elements)
        
        # Run test num trials
        for trial in range(num_trials):
            # Generate random numbers
            a = [i for i in range(num_elements)]
            random.shuffle(a)

            # Create priority queue
            pq = PriorityQueue()

            # Start timer
            start_time = time.time()
            
            # Insert elements in PQ
            for x in a:
                # Insert element and priority
                pq.insert_or_update(x, str(x))

            
            # Set failed flag
            failed_trial = False

            # Testing extraction (in order)
            for i in range(num_elements):
                # Get item
                item = pq.extract()
                priority = item[0]
                data = item[1]

                # Check item
                if priority != i:
                    # Set failed flag
                    failed_trial = True

                    # Print error
                    print('      FAIL: Element #%d is %d' % (i, priority))

                    # Break trial
                    break

            # Check empty PQ should return None
            item = pq.extract()
            if item != None:
                    # Set failed flag
                    failed_trial = True

                    # Print error
                    print('      FAIL: Empty PQ should have returned NONE')

            # End timer and calculate ellapsed time
            end_time = time.time()
            ellapsed_time = end_time - start_time
            
            # Print test result
            if failed_trial:
                # Print failed trial
                print('   Trial #%2d: FAIL' % (trial + 1))
            else:
                 # Print success trial
                print('   Trial #%2d: OK  -- ET = %6.3f' % ((trial + 1), ellapsed_time))

            # Update total time
            total_time += ellapsed_time

        # Compute average time
        avg_time = total_time / num_trials
    
        # Print average time
        print('Average time = %6.2f' % avg_time)
        print()
                      



def test_timed_insertion_update_extraction(elements, num_trials):
    # Show test header
    print()
    print('---------------------------------------------------')
    print('  TESTING TIMED INSERTION, UPDATE  AND EXTRACTION  ')
    print('---------------------------------------------------')
    print()

    for num_elements in elements:
        # Init total elapsed time
        total_time = 0.0

        # Print header
        print('Number of elements = %d' % num_elements)
        
        # Run test num trials
        for trial in range(num_trials):
            # Empty insertion list
            a = []
        
            # Generate random numbers and three types of priorities
            for i in range(num_elements):
                a.append((i + 0 * num_elements, str(i)))
                a.append((i + 1 * num_elements, str(i)))
                a.append((i + 2 * num_elements, str(i)))

            random.shuffle(a)

            # Start timer
            start_time = time.time()
            
            # Create priority queue
            pq = PriorityQueue()

            # Insert elements in PQ
            for x in a:
                # Get item and priority
                priority, data = x
            
                # Insert element and priority
                pq.insert_or_update(priority, data)

            # Generate random numbers
            #a = [i for i in range(num_elements)]
            #random.shuffle(a)

            # Create priority queue
            #pq = PriorityQueue()

            
            
            # Insert elements in PQ
            #for x in a:
                # Insert element and priority
                #pq.insert_or_update(x, str(x))

            
            # Set failed flag
            failed_trial = False

            # Testing extraction (in order)
            for i in range(num_elements):
                # Get item
                item = pq.extract()
                priority = item[0]
                data = item[1]

                # Check item
                if priority != i:
                    # Set failed flag
                    failed_trial = True

                    # Print error
                    print('      FAIL: Element #%d is %d' % (i, priority))

                    # Break trial
                    break

            # Check empty PQ should return None
            item = pq.extract()
            if item != None:
                    # Set failed flag
                    failed_trial = True

                    # Print error
                    print('      FAIL: Empty PQ should have returned NONE')

            # End timer and calculate ellapsed time
            end_time = time.time()
            ellapsed_time = end_time - start_time
            
            # Print test result
            if failed_trial:
                # Print failed trial
                print('   Trial #%2d: FAIL' % (trial + 1))
            else:
                 # Print success trial
                print('   Trial #%2d: OK  -- ET = %6.3f' % ((trial + 1), ellapsed_time))

            # Update total time
            total_time += ellapsed_time

        # Compute average time
        avg_time = total_time / num_trials
    
        # Print average time
        print('Average time = %6.2f' % avg_time)
        print()



if __name__ == '__main__':

    # Test insertion & extraction
    test_insertion_extraction(1000, 15)

    # Test insertion, update & extraction
    test_insertion_update_extraction(1000, 15)

    # Test timed insertion and extraction
    elements = [1000, 2000, 5000, 10000]
    num_trials = 5
    test_timed_insertion_extraction(elements, num_trials)

    # Test timed insertion, update and extraction
    elements = [1000, 2000, 5000, 10000]
    num_trials = 5
    test_timed_insertion_update_extraction(elements, num_trials)
