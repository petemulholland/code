#---
# Excerpted from "Seven Languages in Seven Weeks",
# update to Tree class to use hashes
#---
class Tree
  attr_accessor :children, :node_name
  
  def initialize(hash)
    @children = []
    @node_name = hash.keys[0]
	hash[@node_name].each { |key, value|
		@children.push( Tree.new({key => value}))
	}
  end
  
  def visit_all(&block)
    visit &block
    children.each {|c| c.visit_all &block}
  end
  
  def visit(&block)
    block.call self
  end
end

ruby_tree = Tree.new( {"granpa" => { "da" => { "me" => {}, "bro" => {}}, "unc" => { "cuz" => {}}}} )

puts "Visiting a node"
ruby_tree.visit {|node| puts node.node_name}
puts

puts "visiting entire tree"
ruby_tree.visit_all {|node| puts node.node_name}

