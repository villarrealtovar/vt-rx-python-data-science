from rx import Observable, Observer

letters = Observable.from_(["Alpha","Beta", "Gamma", "Delta", "Epsilon"])

class MySubscriber(Observer):
	
	def on_next(self, value):
		print(value)

	def on_completed(self):
		print("Done!")

	def on_error(self, error):
		print(error)

''' Making the subscribe with the class. To run, uncommented the following line'''
#letters.subscribe(MySubscriber())

''' Making the subscribe with lambda function. I create
the Subscriber on the fly, so I do not need MySubscriber class anymore '''
letters.subscribe(on_next=lambda s: print(s), 
				  on_completed=lambda: print("Done!"), 
				  on_error=lambda e: print(e))