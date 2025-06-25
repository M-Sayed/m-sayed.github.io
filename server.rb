#!/usr/bin/env ruby
# Simple Ruby HTTP server for local development

require 'webrick'
require 'launchy'

PORT = 8000
ROOT = File.expand_path(File.dirname(__FILE__))

# Configure server
server = WEBrick::HTTPServer.new(
  Port: PORT,
  DocumentRoot: ROOT,
  AccessLog: [],
  Logger: WEBrick::Log.new(File.open(File::NULL, 'w'))
)

# Custom mime types for better development experience
WEBrick::HTTPUtils::DefaultMimeTypes['js'] = 'application/javascript'
WEBrick::HTTPUtils::DefaultMimeTypes['mjs'] = 'application/javascript'
WEBrick::HTTPUtils::DefaultMimeTypes['json'] = 'application/json'

# Mount root
server.mount('/', WEBrick::HTTPServlet::FileHandler, ROOT)

# Trap signals for graceful shutdown
['INT', 'TERM'].each do |signal|
  trap(signal) do
    puts "\n\n⏹️  Shutting down server..."
    server.shutdown
  end
end

# Start server
puts "\n🚀 Server running at http://localhost:#{PORT}"
puts "📁 Serving directory: #{ROOT}"
puts "Press Ctrl+C to stop the server\n\n"

# Open browser after server starts
Thread.new do
  sleep(1)
  begin
    Launchy.open("http://localhost:#{PORT}")
  rescue
    # If launchy gem is not installed, just continue
    puts "💡 Tip: Install 'launchy' gem to auto-open browser: gem install launchy"
  end
end

# Start the server
server.start