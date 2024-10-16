# Property based testing with Hypothesis

The [website](https://hypothesis.works) of the Hypothesis project boldly asserts:

> *Normal “automated” software testing is surprisingly manual. Every scenario the computer runs, someone had to write by hand. Hypothesis can fix this.*

While it's debatable whether property-based testing should fully replace the manual parametrization of tests with different inputs and outputs, there's no doubt that Hypothesis is a powerful tool for uncovering bugs nobody would even have considered looking for. In fact, during its development, the authors of Hypothesis accidentally discovered countless bugs in CPython and libraries, thus coining the term *"The Curse of Hypothesis"*.

The framework, although incredibly powerful, might seem overwhelming at first. In this talk, I will demonstrate how even simply throwing random strings at functions can reveal surprising bugs. From there, we'll progress towards generating more complex data, which will be less daunting than it initially appears. You'll also see how Hypothesis seamlessly integrates with various ecosystems and can be a valuable tool in any developer's toolkit.
