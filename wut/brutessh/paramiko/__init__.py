# Copyright (C) 2003-2005 Robey Pointer <robey@lag.net>
#
# This file is part of paramiko.
#
# Paramiko is free software; you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 2.1 of the License, or (at your option)
# any later version.
#
# Paramiko is distrubuted in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Paramiko; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA.

"""
I{Paramiko} (a combination of the esperanto words for "paranoid" and "friend")
is a module for python 2.3 or greater that implements the SSH2 protocol for
secure (encrypted and authenticated) connections to remote machines.  Unlike
SSL (aka TLS), the SSH2 protocol does not require heirarchical certificates
signed by a powerful central authority.  You may know SSH2 as the protocol that
replaced C{telnet} and C{rsh} for secure access to remote shells, but the
protocol also includes the ability to open arbitrary channels to remote
services across an encrypted tunnel.  (This is how C{sftp} works, for example.)

To use this package, pass a socket (or socket-like object) to a L{Transport},
and use L{start_server <Transport.start_server>} or
L{start_client <Transport.start_client>} to negoatite
with the remote host as either a server or client.  As a client, you are
responsible for authenticating using a password or private key, and checking
the server's host key.  I{(Key signature and verification is done by paramiko,
but you will need to provide private keys and check that the content of a
public key matches what you expected to see.)}  As a server, you are
responsible for deciding which users, passwords, and keys to allow, and what
kind of channels to allow.

Once you have finished, either side may request flow-controlled L{Channel}s to
the other side, which are python objects that act like sockets, but send and
receive data over the encrypted session.

Paramiko is written entirely in python (no C or platform-dependent code) and is
released under the GNU Lesser General Public License (LGPL).

Website: U{http://www.lag.net/paramiko/}

@version: 1.5.2 (rhydon)
@author: Robey Pointer
@contact: robey@lag.net
@license: GNU Lesser General Public License (LGPL)
"""

import sys

if sys.version_info < (2, 2):
    raise RuntimeError('You need python 2.2 for this module.')


__author__ = "Robey Pointer <robey@lag.net>"
__date__ = "04 Dec 2005"
__version__ = "1.5.2 (rhydon)"
__version_info__ = (1, 5, 2)
__license__ = "GNU Lesser General Public License (LGPL)"


import transport, auth_handler, channel, rsakey, dsskey, message
import ssh_exception, file, packet, agent, server, util
import sftp_client, sftp_attr, sftp_handle, sftp_server, sftp_si

from transport import randpool, SecurityOptions, Transport
from auth_handler import AuthHandler
from channel import Channel, ChannelFile
from ssh_exception import SSHException, PasswordRequiredException, BadAuthenticationType
from server import ServerInterface, SubsystemHandler, InteractiveQuery
from rsakey import RSAKey
from dsskey import DSSKey
from sftp import SFTPError, BaseSFTP
from sftp_client import SFTP, SFTPClient
from sftp_server import SFTPServer
from sftp_attr import SFTPAttributes
from sftp_handle import SFTPHandle
from sftp_si import SFTPServerInterface
from sftp_file import SFTPFile
from message import Message
from packet import Packetizer
from file import BufferedFile
from agent import Agent, AgentKey
from pkey import PKey

# fix module names for epydoc
for x in [Transport, SecurityOptions, Channel, SFTPServer, SSHException, \
          PasswordRequiredException, BadAuthenticationType, ChannelFile, \
          SubsystemHandler, AuthHandler, RSAKey, DSSKey, SFTPError, \
          SFTP, SFTPClient, SFTPServer, Message, Packetizer, SFTPAttributes, \
          SFTPHandle, SFTPServerInterface, BufferedFile, Agent, AgentKey, \
          PKey, BaseSFTP, SFTPFile, ServerInterface]:
    x.__module__ = 'paramiko'

from common import AUTH_SUCCESSFUL, AUTH_PARTIALLY_SUCCESSFUL, AUTH_FAILED, \
     OPEN_SUCCEEDED, OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED,  OPEN_FAILED_CONNECT_FAILED, \
     OPEN_FAILED_UNKNOWN_CHANNEL_TYPE, OPEN_FAILED_RESOURCE_SHORTAGE

from sftp import SFTP_OK, SFTP_EOF, SFTP_NO_SUCH_FILE, SFTP_PERMISSION_DENIED, SFTP_FAILURE, \
     SFTP_BAD_MESSAGE, SFTP_NO_CONNECTION, SFTP_CONNECTION_LOST, SFTP_OP_UNSUPPORTED

__all__ = [ 'Transport',
            'SecurityOptions',
            'SubsystemHandler',
            'Channel',
            'RSAKey',
            'DSSKey',
            'Agent',
            'Message',
            'SSHException',
            'PasswordRequiredException',
            'BadAuthenticationType',
            'SFTP',
            'SFTPFile',
            'SFTPHandle',
            'SFTPClient',
            'SFTPServer',
            'SFTPError',
            'SFTPAttributes',
            'SFTPServerInterface'
            'ServerInterface',
            'BufferedFile',
            'Agent',
            'AgentKey',
            'rsakey',
            'dsskey',
            'pkey',
            'message',
            'transport',
            'sftp',
            'sftp_client',
            'sftp_server',
            'sftp_attr',
            'sftp_file',
            'sftp_si',
            'sftp_handle',
            'server',
            'file',
            'agent',
            'util' ]
