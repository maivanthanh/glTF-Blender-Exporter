# Copyright (c) 2017 The Khronos Group Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#
# Imports
#

import time

#
# Globals
#

g_profile_started = False
g_profile_start = 0.0
g_profile_end = 0.0
g_profile_delta = 0.0

#
# Functions
#

def print_console(level,
                  output):
    print(level + ': ' + output)


def print_newline():
    print()


def print_timestamp(output = None):
    final_output = str(time.time())
    
    if output is not None:
        final_output = output + ' ' + final_output
    
    print_console('TIMESTAMP', final_output)
    

def profile_start():
    global g_profile_start
    global g_profile_started
    
    if g_profile_started:
        print_console('ERROR', 'Profiling already started')
        return
        
    g_profile_started = True
    
    g_profile_start = time.time()


def profile_end(label = None):
    global g_profile_end
    global g_profile_delta
    global g_profile_started
    
    if not g_profile_started:
        print_console('ERROR', 'Profiling not started')
        return
    
    g_profile_started = False

    g_profile_end = time.time()
    g_profile_delta = g_profile_end - g_profile_start
    
    output = str(g_profile_delta)
    
    if label is not None:
        output = output + '(' + label + ')'    

    print_console('PROFILE', output)
